from book import Book
from msgutils import send_msg, recv_msg
import pickle
import socket

while True:
    with socket.socket() as sock:
        sock.connect(('localhost', 12342))
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
        send_msg(sock, choice.encode(encoding='866'))

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
            send_msg(sock, request_book_id.encode(encoding='866'))
            send_msg(sock, request_name_id.encode(encoding='866'))

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
            send_msg(sock, id_b.encode(encoding='866'))
            send_msg(sock, name.encode(encoding='866'))
            send_msg(sock, author.encode(encoding='866'))
            send_msg(sock, year.encode(encoding='866'))

        if choice == '7':
            request3_book_id = input('Введите ID книги которую хотите удалить: ')
            if not request3_book_id.isnumeric():
                print('Ошибка, вы ввели не число!')
            send_msg(sock, request3_book_id.encode(encoding='866'))

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
            send_msg(sock, id_r.encode(encoding='866'))
            send_msg(sock, name.encode(encoding='866'))
            send_msg(sock, surname.encode(encoding='866'))
            send_msg(sock, age.encode(encoding='866'))

        if choice == '9':
            exit()
