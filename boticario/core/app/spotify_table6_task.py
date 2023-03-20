from boticario.core.app.task import Task
from boticario.core.dpo.spotify_dpo import SpotifyDpo
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyTable6Task(Task):
    def create_table(self):
        SpotifyDpo.create_table_with_full_extraction()

    def run(self):
        self.create_table()
