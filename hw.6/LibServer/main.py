from Lib import Library
from book import Book
from reader import Reader
from msgutils import send_msg, recv_msg
import pickle
import socket

lib = Library()
lib.init_from_files('books_availible.txt', 'reader_list.txt')
sock = socket.socket()
sock.bind(('', 12342))
sock.listen(2)
conn, _ = sock.accept()
"""
достал с цикла подключение
"""
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
    send_msg(conn, pickle.dumps(menu))
    ret = recv_msg(conn).decode(encoding='866')

    if not ret:
        print('Ошибка , нет номера команды!')
        exit()
    if ret == '1':
        send_msg(conn, pickle.dumps(lib.print_all_books()))

    if ret == '2':
        send_msg(conn, pickle.dumps(lib.print_list_books_available()))

    if ret == '3':
        send_msg(conn, pickle.dumps(lib.print_list_books_not_available()))

    if ret == '4':
        request_book_id = recv_msg(conn).decode(encoding='866')
        request_name_id = recv_msg(conn).decode(encoding='866')
        msg = lib.give_book(int(request_book_id), int(request_name_id))
        send_msg(conn, pickle.dumps(msg))

    if ret == '5':
        request_book_id = recv_msg(conn).decode(encoding='866')
        request_name_id = recv_msg(conn).decode(encoding='866')
        msg = lib.return_book(int(request_book_id), int(request_name_id))
        send_msg(conn, pickle.dumps(msg))

    if ret == '6':
        id_b = recv_msg(conn).decode(encoding='866')
        name = recv_msg(conn).decode(encoding='866')
        author = recv_msg(conn).decode(encoding='866')
        year = recv_msg(conn).decode(encoding='866')
        msg = lib.add_book(Book(int(id_b), name, author, int(year)))
        send_msg(conn, pickle.dumps(msg))

    if ret == '7':
        request3_book_id = recv_msg(conn).decode(encoding='866')
        msg = lib.remove_book(int(request3_book_id))
        send_msg(conn, pickle.dumps(msg))

    if ret == '8':
        id_r = recv_msg(conn).decode(encoding='866')
        name = recv_msg(conn).decode(encoding='866')
        surname = recv_msg(conn).decode(encoding='866')
        age = recv_msg(conn).decode(encoding='866')
        msg = lib.add_reader(Reader(int(id_r), name, surname, int(age)))
        send_msg(conn, pickle.dumps(msg))

    if ret == '0':
        exit()








