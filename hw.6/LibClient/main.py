from book import Book
from msgutils import send_msg, recv_msg
import pickle
import socket
with socket.socket() as sock:
    sock = socket.socket()
    sock.connect(('localhost', 12345))
while True:
    menu = recv_msg(sock)

    if not menu:
        print('Ошибка, нет меню!')
        exit()
    menu = pickle.loads(menu)
    print(menu)

    choice = (input("Введите номер команды: "))
    if not choice.isnumeric():
        print('Ошибка, вы ввели не число!')
        exit()
    send_msg(sock, choice.encode())

    if choice in ('1', '2', '3'):
        b_books = recv_msg(sock)
        if not b_books:
            print('Ошибка, нет книг!')
            exit()
        print('Список книг:')
        books = pickle.loads(b_books)
        for book in books:
            print(book)

    if choice in ('4', '5'):
        request_book_id = input('Введите ID книги: ')
        if not request_book_id.isnumeric():
            print('Ошибка, вы ввели не число!')
            exit()
        request_name_id = input('Введите ID читателя: ')
        if not request_name_id.isnumeric():
            print('Ошибка, вы ввели не число!')
            exit()
        send_msg(sock, request_book_id.encode())
        send_msg(sock, request_name_id.encode())
        #answer = pickle.loads(recv_msg(sock))
        print(pickle.loads(recv_msg(sock)))

    if choice == '6':
        id_b = input('Введите ID Книги: ')
        if not id_b.isnumeric():
            print('Ошибка, вы ввели не число!')
            exit()
        name = input('Введите название Книги: ')
        author = input('Введите Автора Книги: ')
        year = input('Введите год Книги: ')

        if not year.isnumeric():
            print('Ошибка, вы ввели не число!')
            exit()
        send_msg(sock, id_b.encode())
        send_msg(sock, name.encode())
        send_msg(sock, author.encode())
        send_msg(sock, year.encode())
        print(pickle.loads(recv_msg(sock)))

    if choice == '7':
        request3_book_id = input('Введите ID книги которую хотите удалить: ')
        if not request3_book_id.isnumeric():
            print('Ошибка, вы ввели не число!')
        send_msg(sock, request3_book_id.encode())
        print(pickle.loads(recv_msg(sock)))

    if choice == '8':
        id_r = input('Введите ID читателя: ')
        if not id_r.isnumeric():
            print('Ошибка, вы ввели не число!')
            exit()
        name = input('Введите имя читателя: ')
        surname = input('Введите фамилию: ')
        age = input('Введите возвраст: ')

        if not age.isnumeric():
            print('Ошибка, вы ввели не число!')
            exit()
        send_msg(sock, id_r.encode())
        send_msg(sock, name.encode())
        send_msg(sock, surname.encode())
        send_msg(sock, age.encode())
        print(pickle.loads(recv_msg(sock)))

    if choice == '0':
        exit()
