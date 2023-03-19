from decouple import config
from psycopg2.extensions import connection, cursor

from boticario.core.helpers.query import QueryFactory
from boticario.core.services.database import with_connected_database
from boticario.logger import get_logging

logging = get_logging(__name__)


class BaseDlo:
    @staticmethod
    @with_connected_database('redshift')
    def copy_data_from_s3_to_redshift(
        connection: connection, cursor: cursor, s3_path: str
    ):
        iam_role = config('REDSHIFT_IAM_ROLE')
        query = QueryFactory(
            'load_parquet',
            table='load.base',
            s3_path=s3_path,
            iam_role=iam_role,
        ).get()
        logging.info('Loading s3 file to load.base redshift table')
        cursor.execute(query)
        connection.commit()
