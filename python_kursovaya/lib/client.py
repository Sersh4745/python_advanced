from .msgutils import send_msg, recv_msg
from .book import Book
from .reader import Reader
import pickle
import socket
from threading import Thread
from .library import Library


class Client(Thread):
    def __init__(self, conn: socket, lib: Library):
        super().__init__()
        self.conn = conn
        self.lib = lib

    def run(self) -> None:
        while True:
            menu = ("\n"
                    " ====== Меню =======" + "\n"
                    "1. Показать все книги" + "\n"
                    "2. Показать книги в наличии" + "\n"
                    "3. Показать книги не в наличии" + "\n"
                    "4. Взять книгу" + "\n"
                    "5. Вернуть книгу" + "\n"
                    "6. Добавить книгу" + "\n"
                    "7. Удалить книгу" + "\n"
                    "8. Добавить читетеля" + "\n"
                    "0. Выход" + "\n")
            send_msg(self.conn, pickle.dumps(menu))
            ret = recv_msg(self.conn).decode()

            if not ret:
                print('Ошибка , нет номера команды!')
                exit()
            if ret == '1':
                send_msg(self.conn, pickle.dumps(self.lib.print_all_books()))

            if ret == '2':
                send_msg(self.conn, pickle.dumps(self.lib.print_list_books_available()))

            if ret == '3':
                send_msg(self.conn, pickle.dumps(self.lib.print_list_books_not_available()))

            if ret == '4':
                request_book_id = recv_msg(self.conn).decode()
                request_name_id = recv_msg(self.conn).decode()
                msg = self.lib.give_book(int(request_book_id), int(request_name_id))
                send_msg(self.conn, pickle.dumps(msg))

            if ret == '5':
                request_book_id = recv_msg(self.conn).decode()
                request_name_id = recv_msg(self.conn).decode()
                msg = self.lib.return_book(int(request_book_id), int(request_name_id))
                send_msg(self.conn, pickle.dumps(msg))

            if ret == '6':
                id_b = recv_msg(self.conn).decode()
                name = recv_msg(self.conn).decode()
                author = recv_msg(self.conn).decode()
                year = recv_msg(self.conn).decode()
                msg = self.lib.add_book(Book(int(id_b), name, author, int(year)))
                send_msg(self.conn, pickle.dumps(msg))

            if ret == '7':
                request3_book_id = recv_msg(self.conn).decode()
                msg = self.lib.remove_book(int(request3_book_id))
                send_msg(self.conn, pickle.dumps(msg))

            if ret == '8':
                id_r = recv_msg(self.conn).decode()
                name = recv_msg(self.conn).decode()
                surname = recv_msg(self.conn).decode()
                age = recv_msg(self.conn).decode()
                msg = self.lib.add_reader(Reader(int(id_r), name, surname, int(age)))
                send_msg(self.conn, pickle.dumps(msg))

            if ret == '0':
                break

