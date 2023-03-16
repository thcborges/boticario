from pathlib import Path

from pandas import DataFrame, concat

from boticario.core.app.task import Task
from boticario.core.helpers.file_reader import FileReader
from boticario.core.helpers.path import (
    DATA_PATH,
    is_processed_path,
    set_processed_folder,
)
from boticario.logger import get_logging

logging = get_logging(__name__)


class BaseIngestionTask(Task):
    __data_path = DATA_PATH / 'raw' / 'base'
    __processed_path = set_processed_folder(__data_path)

    def __is_file_to_process(self, file: Path) -> bool:
        return file.is_file() and not is_processed_path(file)

    def __list_files(self):
        logging.info('Listing base files to process')
        return [
            file
            for file in self.__data_path.glob('**/*')
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
        return concat(data_frames)

    def run(self):
        logging.info('Base Ingestion')
        files = self.__list_files()
        logging.debug('Files to process: %s', str(files))
        data_frame = self.__read_files(files)
