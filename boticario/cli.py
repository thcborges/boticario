import traceback

import click

from boticario import (
    BaseIngestionTask,
    BaseTable1Task,
    BaseTable2Task,
    BaseTable3Task,
    BaseTable4Task,
    SpotifyDataHackersExtract50Task,
)
from boticario.core.services.spotify_api import SpotifyAPI
from boticario.logger import config_logger, get_logging

logging = get_logging(__name__)


@click.group()
def main():
    config_logger()


@main.command()
def base_ingestion_task():
    logging.info('base ingestion task')
    try:
        BaseIngestionTask().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())


@main.command()
def base_create_table1_task():
    logging.info('base create table 1')
    try:
        BaseTable1Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())


@main.command()
def base_create_table2_task():
    logging.info('base create table 2')
    try:
        BaseTable2Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())


@main.command()
def base_create_table3_task():
    logging.info('base create table 3')
    try:
        BaseTable3Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())


@main.command()
def base_create_table4_task():
    logging.info('base create table 4')
    try:
        BaseTable4Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())


@main.command
def base_task_group():
    logging.info('base ingestion task')
    try:
        BaseIngestionTask().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())

    logging.info('base create table 1')
    try:
        BaseTable1Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())

    logging.info('base create table 2')
    try:
        BaseTable2Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())

    logging.info('base create table 3')
    try:
        BaseTable3Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())

    logging.info('base create table 4')
    try:
        BaseTable4Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())


@main.command()
def spotify():
    logging.info('base create table 4')
    try:
        SpotifyDataHackersExtract50Task().run()
    except BaseException as error:
        logging.error(str(error))
        logging.error(traceback.format_exc())
