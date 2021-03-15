from lib import Library
import socket
from client import Client


class Server:
    def __init__(self, ip: str, port: int, lib: Library):
        self.ip = ip
        self.port = port
        self.lib = lib

    def st_server(self):
        with socket.socket() as sock:
            sock.bind((self.ip, self.port))
            sock.listen(1)
            while True:
                conn, _ = sock.accept()
                client_thread = Client(conn, self.lib)
                client_thread.start()


if __name__ == '__main__':
    lib = Library()
    lib.init_from_files('books_availible.txt', 'reader_list.txt')
    server = Server('', 12345, lib)
    server.st_server()
