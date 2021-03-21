from server import *
from client import *
from threading import Thread


if __name__ == '__main__':
    print('Start!')
    start = time()
    server = Thread(target=server, args=())
    client = Thread(target=client, args=())
    server.start()
    client.start()
    server.join()
    client.join()
    print(f'Total time is: {time() - start}')
