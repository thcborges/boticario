from boticario.core.app.task import Task
from boticario.core.dpo.spotify_dpo import SpotifyDpo
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyTable5Task(Task):
    def create_table(self):
        SpotifyDpo.create_table_with_first_50_records()

    def run(self):
        self.create_table()
