from pathlib import Path

from boticario.core.helpers.file_reader.excel_reader import ExcelReader
from boticario.core.helpers.file_reader.reader import Reader


class FileReader:
    __readers = {'.xlsx': ExcelReader}

    def __init__(self, filename: Path | str):
        self.filename: Path = Path(filename)

    def get_reader(self) -> Reader:
        suffix = self.filename.suffix
        ReaderCls = self.__readers.get(suffix)

        if issubclass(ReaderCls, Reader):
            raise NotImplementedError('There is no reader for {suffix} files')

        return ReaderCls(self.filename)
