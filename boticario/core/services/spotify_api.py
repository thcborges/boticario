from decouple import config
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from boticario.logger import get_logging

logging = get_logging(__name__)


SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = config('SPOTIFY_REDIRECT_URI', 'http://localhost:8080')
SPOTIFY_MAX_SEARCH_RECORDS = 50


class SpotifyAPI:
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
    )
    sp = Spotify(auth_manager=auth_manager)

    def get_episodes(self, query: str, amount: int) -> list[dict]:
        result = []
        while (limit := min(amount, SPOTIFY_MAX_SEARCH_RECORDS)) > 0:
            logging.info(
                'Extracting %d data from Spotify API. Missing %d records',
                limit,
                amount,
            )
            data = self.sp.search(
                query, type='episode', limit=limit, offset=len(result)
            )
            episodes = data.get('episodes', {})

            if not episodes:
                return result

            items = episodes.get('items', [])
            if not items:
                return result

            result += items
            amount -= len(items)
        return result
