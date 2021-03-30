from base_class_sql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Reader(Base):
    __tablename__ = 'readers'

    def __init__(self, id: int, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.books = []

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f'{self.id}) {self.name} {self.surname}, {self.age}.'
