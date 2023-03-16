from abc import ABC, abstractmethod
from pathlib import Path

from pandas import DataFrame


class Reader(ABC):
    def __init__(self, filename: Path):
        self.filename = filename

    @abstractmethod
    def read_to_pandas(self, **kwargs) -> DataFrame:
        ...
