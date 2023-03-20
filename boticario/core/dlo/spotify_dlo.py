from decouple import config
from pandas import DataFrame
from psycopg2.extensions import connection, cursor

from boticario.core.helpers.query import QueryFactory
from boticario.core.services.database import with_connected_database
from boticario.core.services.s3 import S3
from boticario.logger import get_logging

logging = get_logging(__name__)


class SpotifyDlo:
    @staticmethod
    @with_connected_database('redshift')
    def copy_data_frame_to_redshift(
        connection: connection,
        cursor: cursor,
        data_frame: DataFrame,
        s3_key: str,
    ):
        logging.info('Uploading file to S3')
        s3_uri = S3('load').upload_data_frame(data_frame, s3_key)

        iam_role = config('REDSHIFT_IAM_ROLE')
        query = QueryFactory(
            'load_parquet',
            table='load.spotify_data_hackers_50',
            s3_path=s3_uri,
            iam_role=iam_role,
        ).get()
        logging.info(
            'Loading s3 file to load.spotify_data_hackers redshift table'
        )
        cursor.execute(query)
        connection.commit()
