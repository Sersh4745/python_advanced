from book import Book
from reader import Reader
from abc import ABC

class SQLstorage(isstoreg, ABC):
    def __init__(self) -> None:
        super().__init__()