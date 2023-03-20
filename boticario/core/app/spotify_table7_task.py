from boticario.core.app.task import Task
from boticario.core.dpo.spotify_dpo import SpotifyDpo
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyTable7Task(Task):
    def create_table(self):
        SpotifyDpo.create_table_with_participation_of_grupo_boticario()

    def run(self):
        self.create_table()
