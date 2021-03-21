import socket
from time import time
import threading
import math
from io import StringIO
file = StringIO()
new_list = []


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    s = int(math.floor(math.sqrt(n)))
    for i in range(3, s + 1, 2):
        if n % i == 0:
            return False
    return True


def write():
    global new_list
    while new_list:
        n = new_list.pop()
        if is_prime(n):
            file.write(str(n) + '\n')


def server():
    global new_list
    print(f'Start server!')
    with socket.socket() as sock:
        sock.bind(('', 12345))
        sock.listen(10)
        while True:
            conn, addr = sock.accept()
            print('connected', addr)
            data = ""
            start = time()
            while True:
                num = conn.recv(4096).decode()
                if not num:
                    break
                data += num
            new_list = eval(data)
            new_list_len = len(new_list)
            print(f'Server list ready in {time() - start}')
            tasks = []
            for i in range(3):
                task = threading.Thread(target=write, args=())
                task.start()
                tasks.append(task)
            for task in tasks:
                task.join()
            break
    with open('test.txt', 'w') as f:
        f.write(file.getvalue())
    print(f'Server time is: {time() - start}')
    print(f'Server counter is: {new_list_len}')
    print(f'')
