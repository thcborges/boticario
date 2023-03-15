import click

from boticario import BaseIngestionTask
from boticario.logger import config_logger, get_logging

logging = get_logging(__name__)


@click.group()
def main():
    config_logger()


@main.command()
def base_ingestion_task():
    logging.info('base ingestion task')
    BaseIngestionTask().run()
