import logging
import logging.config

import yaml
from decouple import config

from boticario.core.helpers.path import get_config_file, get_logging_path


def config_logger():
    logging_path = get_logging_path()
    config_file = get_config_file('logger')

    with open(config_file) as file:
        logging_config = yaml.safe_load(file.read())
    for handler in logging_config.get('handlers').values():
        if handler.get('filename'):
            handler['filename'] = logging_path / handler['filename']

    logging_config['handlers']['console']['level'] = config(
        'LOGGING_LEVEL', 'ERROR'
    )

    logging.config.dictConfig(logging_config)


def get_logging(name) -> logging.Logger:
    return logging.getLogger(name)
