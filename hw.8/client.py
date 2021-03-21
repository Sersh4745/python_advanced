import socket
from time import time


def is_prime(n):
    """
    нашел на habr.com
    самый быстрый способ генирации
    """
    x = list(range(n + 1))
    x[1] = 0
    spisok = []
    i = 2
    while i <= n:
        if x[i] != 0:
            spisok.append(x[i])
            for j in range(i, n + 1, i):
                x[j] = 0
        i += 1
    return spisok


def client():
    start = time()
    prime_list = is_prime(2000000)
    prime_len = len(prime_list)
    with socket.socket() as sock:
        sock.connect(('localhost', 12345))
        sock.send(str(prime_list).encode())
    print(f'Client time is: {time() - start}')
    print(f'Client counter is: {prime_len}')
    print(f'')
