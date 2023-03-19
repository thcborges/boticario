from psycopg2.extensions import connection, cursor

from boticario.core.helpers.query import QueryFactory
from boticario.core.services.database import with_connected_database
from boticario.logger import get_logging

logging = get_logging(__name__)


class BaseDpo:
    @staticmethod
    @with_connected_database('redshift')
    def create_table_aggregating_sales_by_year_month(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table1',
        ).get()
        logging.info('Creating table aggregating sales by year/month')
        cursor.execute(query)
        connection.commit()

    @staticmethod
    @with_connected_database('redshift')
    def create_table_aggregating_sales_by_brand_and_type(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table2',
        ).get()
        logging.info('Creating table aggregating sales by brand and type')
        cursor.execute(query)
        connection.commit()

    @staticmethod
    @with_connected_database('redshift')
    def create_table_aggregating_sales_by_brand_year_month(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table3',
        ).get()
        logging.info(
            'Creating table aggregating sales by brand and year/month'
        )
        cursor.execute(query)
        connection.commit()

    @staticmethod
    @with_connected_database('redshift')
    def create_table_aggregating_sales_by_type_year_month(
        connection: connection, cursor: cursor
    ):
        query = QueryFactory(
            'create_table4',
        ).get()
        logging.info('Creating table aggregating sales by type and year/month')
        cursor.execute(query)
        connection.commit()
