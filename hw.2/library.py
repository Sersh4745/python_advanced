from book import Book
from reader import Reader

import os.path


class Library:
    def __init__(self, book_list = None, reader_list = None):
        self.books = book_list
        self.readers = reader_list

    def init_from_files(self, books_file: str = None, readers_file: str = None) -> None:
        """
        Это функция заполнения библиотеки из файлов

        :param books_file: файл со списком книг
        :param readers_file: файл со списком читателей
        :return: None
        """
        if self.books is None: self.books = []
        if self.readers is None: self.readers = []

        if books_file is not None and os.path.exists(books_file):
            with open(books_file, 'r', encoding='utf-8') as f:
                for line in f:
                    data_list = line.strip().split('$!$')

                    if len(data_list) == 4 and data_list[0].isnumeric():
                        self.books.append(Book(
                            int(data_list[0]),  # id книги
                            data_list[1],       # название книги
                            data_list[2],       # автор книги
                            data_list[3],       # год издания
                        ))

        if readers_file is not None and os.path.exists(readers_file):
            with open(readers_file, 'r', encoding='utf-8') as file:
                for line in file:
                    name_list = line.strip().split('$!$')

                    if len(name_list) == 4 and name_list[0].isnumeric():
                        self.readers.append(Reader(
                            int(name_list[0]),  # id 
                            name_list[1],       # имя
                            name_list[2],       # фамилия
                            name_list[3],       # возраст
                        ))

    def add_book(self, obj_book: Book) -> None:
        """
        # @todo напиши коммент

        :param obj_book:
        :return:
        """
        all_books_id = [book.id for book in self.books]
        if obj_book[0] in all_books_id:
            print(f'Ошибка , книга с таким ID "{obj_book[0]}" уже есть в библиотеке! ')
            return

        self.books.append(Book(
                            int(obj_book[0]),  # id книги
                            obj_book[1],       # название книги
                            obj_book[2],       # автор книги
                            obj_book[3],       # год издания
                        ))
        print(f'Поздравляем, книга "{obj_book[0]}" добавлена в библиотеку')

    def remove_book(self, id_book: int) -> None:
        """
        Удаляет книгу из библиотеки

        :param id_book: id книги, которую нужно удалить
        :return: None
        """
        if id_book.isnumeric():
            all_books_id = [book.id for book in self.books]
            if int(id_book) not in all_books_id:
                print(f'Ошибка, книга с таким ID  "{id_book}" не найдена')
            for book in self.books:
                if int(book.id) == int(id_book):
                    self.books.remove(book)
                    print(f'Книга  "{book.title}" была удалена')
        else:
            print('Введите числом')
                
    def add_reader(self, obj_reader: Reader) -> None:
        """
        # @todo Коммент!

        :param obj_reader:
        :return:
        """
        all_readers_id = [reader.id for reader in self.readers]
        if obj_reader[0] in all_readers_id:
            print(f'Ошибка, читатель с таким ID "{obj_reader[0]}" уже существует!')
            return
        #self.readers.append(obj_reader)
        self.readers.append(Reader(
                            int(obj_reader[0]),  # id 
                            obj_reader[1],       # имя
                            obj_reader[2],       # фамилия
                            obj_reader[3],       # возраст
                        ))
        print(f'Поздравляем, читатель с ID {obj_reader[0]} зарегестрирован.')

    def print_all_books(self) -> None:
        """
        Выводит список всех книг, которые зарегистрированы в библиотеке

        :return: None
        """
        print('Список книг :')
        for book in self.books:
            print(book)

    def print_list_books_available(self) -> None:
        """
        Выводит список книг, которые находятся в библиотеке

        :return: None
        """
        print('Спсиок книг в наличии:')

        for book in self.books:
            if book.id_reader == None:
                print(book)


    def print_list_books_not_available(self) -> None:
        """
        Выводит список книг, которые находятся на руках у читателей

        :return: None
        """
        print('Спсиок книг не в наличии:')
        for book in self.books:
            if book.id_reader != None:
                print(book)


    def give_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция выдачи книги читателю

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        if id_book.isnumeric() and id_reader.isnumeric():
            all_books_id = [book.id for book in self.books]
            if int(id_book) not in all_books_id:
                print(f'Ощибка, книги с таким ID {id_book} нет!')

            all_readers_id = [reader.id for reader in self.readers]
            if int(id_reader) not in all_readers_id:
                print(f'Ошибка, пользователя с таким ID {id_reader} нет!')

            for book in self.books:
                for reader in self.readers:
                    if book.id == int(id_book):
                        if reader.id == int(id_reader):
                            book.id_reader = int(id_reader)
                            print('Поздравляем книга выдана')
        else:
            print('Введите числом')
       
    def return_book(self, id_book: int, id_reader: int) -> None:
        """
        Функция возврата книги в библиотеку

        :param id_book: id книги
        :param id_reader: id читателя
        :return:
        """
        if id_book.isnumeric() and id_reader.isnumeric():
            for book in self.books:
                if int(book.id) == int(id_book):
                    if int(book.id_reader) == int(id_reader):
                        book.id_reader = None    
                        print('Поздравляем Вы вернули книгу')
                    else:
                        print(f'Ощибка, книги с таким ID {id_book} нет!')
        else:
            print('Введите числом')
