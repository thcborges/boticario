from datetime import datetime

from pandas import DataFrame

from boticario.core.app.task import Task
from boticario.core.dao.spotify_dao import SpotifyDao
from boticario.core.dlo.spotify_dlo import SpotifyDlo
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyDataHackersExtractFullTask(Task):
    __s3_path = 'spotify_data_hackers_full'

    def __get_api_data(self) -> DataFrame:
        logging.info('Getting data from spotify API')
        data_frame = SpotifyDao.get_records_to_data_hackers_search()
        data_frame.to_csv('data_hackers.csv', index=False)
        return data_frame

    def __load_data(self, data_frame: DataFrame):
        logging.info('Loading data to redshift')
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        s3_key = (
            f'{self.__s3_path}/spotify_data_hackers_full_{timestamp}.parquet'
        )
        SpotifyDlo.copy_data_frame_to_redshift(data_frame, s3_key)

    def run(self):
        data_frame = self.__get_api_data()
        self.__load_data(data_frame)
