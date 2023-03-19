from datetime import datetime
from pathlib import Path

from pandas import DataFrame, concat

from boticario.core.app.task import Task
from boticario.core.dlo.base_dlo import BaseDlo
from boticario.core.helpers.file_reader import FileReader
from boticario.core.helpers.path import (
    DATA_PATH,
    get_s3_uri,
    is_processed_path,
    set_processed_folder,
)
from boticario.logger import get_logging

logging = get_logging(__name__)


class BaseIngestionTask(Task):
    __raw_path = DATA_PATH / 'raw' / 'base'
    __processed_raw_path = set_processed_folder(__raw_path)
    __load_path = DATA_PATH / 'load' / 'base'

    def __is_file_to_process(self, file: Path) -> bool:
        return file.is_file() and not is_processed_path(file)

    def __list_files(self):
        logging.info('Listing base files to process')
        return [
            file
            for file in self.__raw_path.glob('**/*')
            if self.__is_file_to_process(file)
        ]

    def __read_files(self, files: list[Path]) -> DataFrame:
        logging.info('Reading base files')
        data_frames = []
        for file in files:
            reader = FileReader(file).get_reader()
            data_frame = reader.read_to_pandas()
            data_frame['filename'] = file.name
            data_frames.append(data_frame)
        if data_frames:
            return concat(data_frames)

    def __create_parquet(self, data_frame: DataFrame):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = self.__load_path / f'base_{timestamp}.parquet'
        data_frame.to_parquet(filename, index=False)
        return filename

    def __load_to_database(self, file_path):
        s3_path = get_s3_uri(file_path)
        BaseDlo.copy_data_from_s3_to_redshift(s3_path)

    def __load_data(self, data_frame: dict[str, DataFrame]):
        logging.info('Creating parquet file')
        parquet_path = self.__create_parquet(data_frame)
        self.__load_to_database(parquet_path)

    def __move_to_process_folder(self, files):
        logging.info('Moving files to processed folder')
        self.__processed_raw_path.mkdir(parents=True, exist_ok=True)
        for file in files:
            file.rename(self.__processed_raw_path / file.name)

    def run(self):
        logging.info('Base Ingestion')
        files = self.__list_files()
        if files:
            logging.debug('Files to process: %s', str(files))
            data_frame = self.__read_files(files)
            self.__load_data(data_frame)
            self.__move_to_process_folder(files)
