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
        res = self.session.query(Book).all()
        a = []
        if res == a:
            for book in self.books:
                self.session.add(book)
            self.session.commit()
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

        res = self.session.query(Reader).all()
        a = []
        if res == a:
            for reader in self.readers:
                self.session.add(reader)
            self.session.commit()
        else:
            pass

    def add_book(self, obj_book: Book) -> None:
        """
        Добавление книги в Библиотеку
        :param obj_book: объект Книга
        :return: None
        """
        all_books_id = [book.id for book in self.session.query(Book)]
        if obj_book.id in all_books_id:
            print(f'Ошибка , книга с таким ID "{obj_book.id}" уже есть в библиотеке! ')
            return
        # Добавим в Базу
        self.session.add(obj_book)
        self.session.commit()
        print(f'Поздравляем, книга "{obj_book.id}" добавлена в библиотеку')

    def remove_book(self, id_book: int) -> None:
        """
        Удаляет книгу из библиотеки

        :param id_book: id книги, которую нужно удалить
        :return: None
        """
        all_books_id = [book.id for book in self.session.query(Book)]
        if id_book not in all_books_id:
            print(f'Ошибка, книга с ID "{id_book}" не найдена')
            return

        for book in self.session.query(Book):
            if book.id == id_book:
                self.session.delete(book)  # Удалим с Базы
                self.session.commit()
                print(f'Книга "{book.title}" была удалена')
                break

    def add_reader(self, obj_reader: Reader) -> None:
        """
        Добавление читателя в библиотеку
        :param obj_reader: Объект Читатель
        :return: None
        """
        all_readers_id = [reader.id for reader in self.session.query(Reader)]
        if obj_reader.id in all_readers_id:
            print(f'Ошибка, читатель с ID "{obj_reader.id}" уже существует!')
            return
        # Добавим в Базу
        self.session.add(obj_reader)
        self.session.commit()
        print(f'Поздравляем, читатель с ID {obj_reader.id} зарегестрирован.')

    def print_all_readers(self) -> None:
        for instance in self.session.query(Reader):  # Выводим с базы
            print(instance)

    def print_all_books(self) -> None:
        """
        Выводит список всех книг, которые зарегистрированы в библиотеке

        :return: None
        """
        print('Список книг:')
        for instance in self.session.query(Book):  # Выводим с базы
            print(instance)

    def print_list_books_available(self) -> None:
        """
        Выводит список книг, которые находятся в библиотеке

        :return: None
        """
        print('Спсиок книг в наличии:')
        for instance in self.session.query(Book).where(Book.id_reader == None):  # is None не работает почему то((
            print(instance)

    def print_list_books_not_available(self) -> None:
        """
        Выводит список книг, которые находятся на руках у читателей

        :return: None
        """
        print('Спсиок книг не в наличии:')
        for instance in self.session.query(Book).where(Book.id_reader != None):  # not None не работает
            print(instance)

    def give_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция выдачи книги читателю

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        all_readers_id = [reader.id for reader in self.session.query(Reader)]
        if id_reader not in all_readers_id:
            print(f'Ошибка, пользователя с ID {id_reader} нет!')
        obj_book = [book.id for book in self.session.query(Book)]
        if id_book not in obj_book:
            print(f'Ошибка, книги с ID {id_book} нет в наличии!')

        for instance in self.session.query(Book).where(Book.id == id_book):  # Выводим с базы
            instance.id_reader = id_reader
            print('Поздравляем, книга выдана!')
        self.session.commit()

    def return_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция возврата книги в библиотеку

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        all_readers_id = [reader.id for reader in self.session.query(Reader)]
        if id_reader not in all_readers_id:
            print(f'Ошибка, пользователя с ID {id_reader} нет!')
        obj_book = [book.id for book in self.session.query(Book)]
        if id_book not in obj_book:
            print(f'Ошибка, книги с ID {id_book} нет в наличии!')

        for instance in self.session.query(Book).where(Book.id == id_book and Book.id_reader == id_reader):  # Выводим с базы
            instance.id_reader = None
            print('Поздравляем Вы вернули книгу')
        self.session.commit()
