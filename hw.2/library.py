from book import Book
from reader import Reader

import os.path


class Library:
    def __init__(self, book_list=None, reader_list=None):
        # тернарный оператор =)
        self.books = book_list if book_list is not None else []
        self.readers = reader_list if reader_list is not None else []

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
                            data_list[1],       # название книги
                            data_list[2],       # автор книги
                            int(data_list[3]),  # год издания
                        ))

        if readers_file is not None and os.path.exists(readers_file):
            with open(readers_file, 'r', encoding='utf-8') as file:
                for line in file:
                    name_list = line.strip().split('$!$')

                    # name_list[0] -> int, т.к. id
                    # name_list[3] -> int, т.к. age
                    if len(name_list) == 4 \
                            and name_list[0].isnumeric() \
                            and name_list[3].isnumeric():
                        self.readers.append(Reader(
                            int(name_list[0]),  # id 
                            name_list[1],  # имя
                            name_list[2],  # фамилия
                            int(name_list[3]),  # возраст
                        ))

    def add_book(self, obj_book: Book) -> None:
        """
        Добавление книги в Библиотеку

        :param obj_book: объект Книга
        :return: None
        """
        all_books_id = [book.id for book in self.books]
        if obj_book.id in all_books_id:
            print(f'Ошибка , книга с таким ID "{obj_book.id}" уже есть в библиотеке! ')
            return

        self.books.append(obj_book)
        print(f'Поздравляем, книга "{obj_book.id}" добавлена в библиотеку')

    def remove_book(self, id_book: int) -> None:
        """
        Удаляет книгу из библиотеки

        :param id_book: id книги, которую нужно удалить
        :return: None
        """
        all_books_id = [book.id for book in self.books]
        if id_book not in all_books_id:
            print(f'Ошибка, книга с ID "{id_book}" не найдена')
            return

        for book in self.books:
            if book.id == id_book:
                self.books.remove(book)
                print(f'Книга "{book.title}" была удалена')

                # ок, а если эта книга у кого-то из читателей???
                # хотя ты и не добавлял книги читателям
                for reader in self.readers:
                    if id_book in reader.books:
                        reader.books.remove(book)
                        break

                break

    def add_reader(self, obj_reader: Reader) -> None:
        """
        Добавление читателя в библиотеку

        :param obj_reader: Объект Читатель
        :return: None
        """
        all_readers_id = [reader.id for reader in self.readers]
        if obj_reader.id in all_readers_id:
            print(f'Ошибка, читатель с ID "{obj_reader.id}" уже существует!')
            return

        self.readers.append(obj_reader)
        print(f'Поздравляем, читатель с ID {obj_reader.id} зарегистрирован.')

    def print_all_books(self) -> None:
        """
        Выводит список всех книг, которые зарегистрированы в библиотеке
        """
        print('Список книг:')
        for book in self.books:
            print(book)

    def print_list_books_available(self) -> None:
        """
        Выводит список книг, которые находятся в библиотеке
        """
        print('Спсиок книг в наличии:')

        for book in self.books:
            if book.id_reader is None:
                print(book)

    def print_list_books_not_available(self) -> None:
        """
        Выводит список книг, которые находятся на руках у читателей
        """
        print('Спсиок книг не в наличии:')
        for book in self.books:
            if book.id_reader is not None:
                print(book)

    def give_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция выдачи книги читателю

        :param id_book: id книги
        :param id_reader: id читателя
        """
        all_books_id = [book.id for book in self.books]
        if id_book not in all_books_id:
            print(f'Ошибка, книги с ID {id_book} нет!')
            return

        all_readers_id = [reader.id for reader in self.readers]
        if id_reader not in all_readers_id:
            print(f'Ошибка, пользователя с ID {id_reader} нет!')
            return

        # твои циклы очень долгие, лучше отдельно!
        obj_book = [book for book in self.books if id_book == book.id][0]

        # и третья проверка =)
        if obj_book.id_reader is not None:
            print(f'Ошибка, книги с ID {id_reader} нет в наличии!')
            return

        # получаем юзера
        obj_reader = [reader for reader in self.readers if id_reader == reader.id][0]

        # выдаем книгу
        obj_book.id_reader = obj_reader.id
        obj_reader.books.append(obj_book.id)
        print('Поздравляем, книга выдана!')

    def return_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция возврата книги в библиотеку

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        all_books_id = [book.id for book in self.books]
        if id_book not in all_books_id:
            print(f'Ошибка, книги с ID {id_book} нет!')
            return

        all_readers_id = [reader.id for reader in self.readers]
        if id_reader not in all_readers_id:
            print(f'Ошибка, пользователя с ID {id_reader} нет!')
            return

        obj_book = [book for book in self.books if id_book == book.id][0]
        if obj_book.id_reader is None:
            print(f'Ошибка, книга с ID {id_reader} и так в библиотеке!')
            return

        obj_reader = [reader for reader in self.readers if id_reader == reader.id][0]
        if obj_book.id_reader != obj_reader.id or obj_book.id not in obj_reader.books:
            print(f'Ошибка, книга с ID {id_reader} находится не у {obj_reader.name}!')
            return

        # возвращаем книгу
        obj_book.id_reader = None
        obj_reader.books.remove(obj_book.id)
        print('Поздравляем Вы вернули книгу')
