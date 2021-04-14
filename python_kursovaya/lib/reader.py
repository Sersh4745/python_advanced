from .base_class_sql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Reader(Base, UserMixin):
    __tablename__ = 'readers'
    # id: int,

    def __init__(self, name: str, surname: str, age: int, email: str, psw: str) -> None:
        # self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        # self.books = []
        self.email = email
        self.psw_hash = generate_password_hash(psw)

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    email = Column(String)
    psw_hash = Column(String)

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.age}, {self.email},{self.psw_hash}.'

    def get_id(self) -> int:
        return self.id

    def check_psw(self, psw: str) -> bool:
        return check_password_hash(self.psw_hash, psw)
