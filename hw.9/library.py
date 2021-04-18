from sqlalchemy.orm import create_session
from book import Book
from reader import Reader
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import Session
import os.path
from base_class_sql import Base


class Library:
    def __init__(self, book_list=None, reader_list=None):
        # тернарный оператор =)
        self.books = book_list if book_list is not None else []
        self.readers = reader_list if reader_list is not None else []
        self.e = create_engine('postgresql://postgres:133113zz@localhost:5432/postgres')
        Base.metadata.create_all(self.e)
        self.session = Session(self.e)

    def init_from_files(self, books_file: str = None, readers_file: str = None) -> None:
        """
        Это функция заполнения библиотеки из файлов

        :param books_file: файл со списком книг
        :param readers_file: файл со списком читателей
        :return: None
        """
        if books_file is not None and os.path.exists(books_file):
            with open(books_file, 'r', encoding='utf-8') as f:
                for line in f:
                    data_list = line.strip().split('$!$')

                    if len(data_list) == 4 and data_list[0].isnumeric():
                        self.books.append(Book(
                            int(data_list[0]),  # id книги
                            data_list[1],  # название книги
                            data_list[2],  # автор книги
                            int(data_list[3]),  # год издания
                        ))
        """
                Проверим таблици на наличие информации
                и если все Ок то запишем туда наши данные
        """
        res = [instance for instance in self.e.execute(f'select * from "books" ')]
        a = []
        if res == a:
            for book in self.books:
                self.e.execute(
                    f'insert into books (id, title, author, year) '
                    f'values(\'{book.id}\', \'{book.title}\', \'{book.author}\', \'{book.year}\');')
        else:
            pass

        if readers_file is not None and os.path.exists(readers_file):
            with open(readers_file, 'r', encoding='utf-8') as file:
                for line in file:
                    name_list = line.strip().split('$!$')

                    if len(name_list) == 4 \
                            and name_list[0].isnumeric() \
                            and name_list[3].isnumeric():
                        self.readers.append(Reader(
                            int(name_list[0]),  # id
                            name_list[1],  # имя
                            name_list[2],  # фамилия
                            int(name_list[3]),  # возраст
                        ))

        res = [instance for instance in self.e.execute(f'select * from "readers" ')]
        a = []
        if res == a:
            for reader in self.readers:
                self.e.execute(
                    f'insert into readers (id, name, surname,age) '
                    f'values(\'{reader.id}\', \'{reader.name}\', \'{reader.surname}\', \'{reader.age}\');')
        else:
            pass

    def add_book(self, obj_book: Book) -> None:
        """
        Добавление книги в Библиотеку
        :param obj_book: объект Книга
        :return: None
        """
        all_books_id = [book.id for book in self.e.execute(f'select * from "books" ')]
        if obj_book.id in all_books_id:
            print(f'Ошибка , книга с таким ID "{obj_book.id}" уже есть в библиотеке! ')
            return
        # Добавим в Базу
        self.e.execute(
            f'insert into books (id, title, author, year) '
            f'values(\'{obj_book.id}\', \'{obj_book.title}\', \'{obj_book.author}\', \'{obj_book.year}\');')
        print(f'Поздравляем, книга "{obj_book.id}" добавлена в библиотеку')

    def remove_book(self, id_book: int) -> None:
        """
        Удаляет книгу из библиотеки

        :param id_book: id книги, которую нужно удалить
        :return: None
        """
        all_books_id = [book.id for book in self.e.execute(f'select * from "books" ')]
        if id_book not in all_books_id:
            print(f'Ошибка, книга с ID "{id_book}" не найдена')
            return
        self.e.execute(f'delete from books where id = {id_book};')
        print(f'Книга "{id_book}" была удалена')

    def add_reader(self, obj_reader: Reader) -> None:
        """
        Добавление читателя в библиотеку
        :param obj_reader: Объект Читатель
        :return: None
        """
        all_readers_id = [reader.id for reader in self.e.execute(f'select * from "readers" ')]
        if obj_reader.id in all_readers_id:
            print(f'Ошибка, читатель с ID "{obj_reader.id}" уже существует!')
            return
        # Добавим в Базу
        self.e.execute(
            f'insert into readers (id, name, surname,age) '
            f'values(\'{obj_reader.id}\', \'{obj_reader.name}\', \'{obj_reader.surname}\', \'{obj_reader.age}\');')
        print(f'Поздравляем, читатель с ID {obj_reader.id} зарегестрирован.')

    def print_all_readers(self) -> None:
        print('Список читателей:')
        for instance in self.e.execute(f'select * from "readers" '):  # Выводим с базы
            print(instance)

    def print_all_books(self) -> None:
        """
        Выводит список всех книг, которые зарегистрированы в библиотеке

        :return: None
        """
        print('Список книг:')
        for instance in self.e.execute(f'select books.id, books.title, books.author, books.year from "books" '):
            print(instance)

    def print_list_books_available(self) -> None:
        """
        Выводит список книг, которые находятся в библиотеке

        :return: None
        """
        print('Спсиок книг в наличии:')
        for instance in self.e.execute(f'select books.id, books.title, books.author, books.year'
                                       f' from "books" where id_reader is NULL'):  # Выводим с базы
            print(instance)

    def print_list_books_not_available(self) -> None:
        """
        Выводит список книг, которые находятся на руках у читателей

        :return: None
        """
        print('Спсиок книг не в наличии:')
        for instance in self.e.execute(f'select books.id, books.title, books.author, books.year'
                                       f' from "books" where id_reader is not NULL'):  # Выводим с базы
            print(instance)

    def give_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция выдачи книги читателю

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        all_readers_id = [reader.id for reader in self.e.execute(f'select * from "readers" ')]
        if id_reader not in all_readers_id:
            print(f'Ошибка, пользователя с ID {id_reader} нет!')
            return
        obj_book = [book.id for book in self.e.execute(f'select * from "books" ')]
        if id_book not in obj_book:
            print(f'Ошибка, книги с ID {id_book} нет в наличии!')
            return
        obj_book2 = [book.id for book in self.e.execute(f'select * from "books" where id_reader is not NULL')]
        if id_book in obj_book2:
            print(f'Книга с ID {id_book} уже на руках')
            return
        else:
            """ блокируем функию ,
                что бы избежать ввода одинакового ID
            """
            self.e.execute(f'update books set id_reader = {id_reader} where id = {id_book};')
            print('Поздравляем, книга выдана!')

    def return_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция возврата книги в библиотеку

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        all_readers_id = [reader.id for reader in self.e.execute(f'select * from "readers" ')]
        if id_reader not in all_readers_id:
            print(f'Ошибка, пользователя с ID {id_reader} нет!')
            return
        obj_book = [book.id for book in self.e.execute(f'select * from "books" ')]
        if id_book not in obj_book:
            print(f'Ошибка, книги с ID {id_book} нет в наличии!')
            return
        obj_book2 = [book.id for book in self.e.execute(f'select * from "books" where id_reader is NULL')]
        if id_book in obj_book2:
            print(f'Книгу с ID {id_book} нельзя вернуть, она уже в библиотеке')
            return
        else:
            self.e.execute(f'update books set id_reader = NULL where id = {id_book} and id_reader = {id_reader};')
            print('Поздравляем Вы вернули книгу')
