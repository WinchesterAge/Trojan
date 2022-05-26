import socket
from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(("localhost", 1111))


s.listen(2)

print('server is listening...')

conn, addr = s.accept()

print(f'{addr} is connected')

while True:
    commamd = input(f'{conn.recv(1024).decode()} ')
    if commamd == '' or commamd == None:
        conn.send('none'.encode())
        continue
    elif commamd == '--exit':
        break
    conn.send(commamd.encode())
    print('sended')
    data = conn.recv(1024).decode()
    print(data)