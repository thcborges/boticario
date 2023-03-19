from pathlib import Path

from boticario.core.helpers.path import QUERY_PATH
from boticario.logger import get_logging

logging = get_logging(__name__)


class QueryFactory:
    __queries = {'load_parquet': QUERY_PATH / 'load_parquet.sql'}

    def __init__(self, query: str, **kwargs) -> None:
        self.__file: Path = self.__queries.get(query)
        self.__kwargs = kwargs
        logging.info('Getting %s query from %s file', query, self.__file)

    def get(self) -> str:
        if not self.__file.is_file():
            logging.error('Requested file %s does not exists', self.__file)
            raise FileNotFoundError(f'Query file "{self.__file} not found"')
        return self.__file.read_text().format(**self.__kwargs)
