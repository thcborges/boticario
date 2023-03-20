from pandas import DataFrame

from boticario.core.services.spotify_api import SpotifyAPI
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyDao:
    @staticmethod
    def get_first_50_records_to_data_hackers_search() -> DataFrame:
        data = SpotifyAPI().get_episodes('data hackers', 50)
        data_frame = DataFrame(data)
        if not data_frame.empty:
            for column in ['external_urls', 'images', 'languages']:
                data_frame[column] = data_frame[column].astype(str)
        return data_frame
