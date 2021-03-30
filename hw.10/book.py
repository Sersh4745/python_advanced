from base_class_sql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = 'books'

    def __init__(self, book_id: int, book_name: str, book_author: str, book_year: int, id_reader=None) -> None:
        self.id = book_id
        self.title = book_name
        self.author = book_author
        self.year = book_year

        self.reader_id = id_reader

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

    id_reader = Column(Integer, ForeignKey('readers.id'))
    reader_ = relationship('Reader', backref='books')

    def __str__(self):
        return f'{self.id}) "{self.title}". {self.author}, {self.year}.'