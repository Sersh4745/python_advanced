from Lib import Book
from msgutils import send_msg, recv_msg
import pickle
import socket
import time

with socket.socket() as sock:
    sock.connect(('localhost', 12343))


    b_books = recv_msg(sock)
    if not b_books:
        print('ERROR')
        exit()

    books = pickle.loads(b_books)

    for book in books:
        print(book)
