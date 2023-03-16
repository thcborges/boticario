from pandas import DataFrame, read_excel

from boticario.core.helpers.file_reader.reader import Reader
from boticario.logger import get_logging

logging = get_logging(__name__)


class ExcelReader(Reader):
    def read_to_pandas(self, **kwargs) -> DataFrame:
        logging.info('Reading %s excel file to pandas', self.filename)
        df = read_excel(self.filename, **kwargs)
        return df
