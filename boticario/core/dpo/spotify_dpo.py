from psycopg2.extensions import connection, cursor

from boticario.core.helpers.query import QueryFactory
from boticario.core.services.database import with_connected_database
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyDpo:
    @staticmethod
    @with_connected_database('redshift')
    def create_table_with_first_50_records(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table5',
        ).get()
        logging.info(
            'Creating table with first 50 records searching for data hackers '
            'from the Spotify API'
        )
        cursor.execute(query)
        connection.commit()

    @staticmethod
    @with_connected_database('redshift')
    def create_table_with_full_extraction(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table6',
        ).get()
        logging.info(
            'Creating table with full extraction searching for data hackers '
            'on Spotify API'
        )
        cursor.execute(query)
        connection.commit()

    @staticmethod
    @with_connected_database('redshift')
    def create_table_with_participation_of_grupo_boticario(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table7',
        ).get()
        logging.info(
            'Creating table from data hackers extraction on Spotify API '
            'with participation of Grupo Boticario'
        )
        cursor.execute(query)
        connection.commit()
