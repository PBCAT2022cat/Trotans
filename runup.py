from socket import *
import sys

s = socket(AF_INET,SOCK_STREAM)
s.connect(('192.168.0.105',12345))
s.setblocking(True)
get = None
try:
    get = s.recv(1024)
    names = get.decode().rstrip()
    get = s.recv(1024)
    lens = int(get.decode().rstrip())
    s.send("good\n".encode())
    writes = s.recv(lens)
    with open(names,'wb') as file:
        file.write(writes)
    s.send("good end\n".encode())
except Exception as r:
    print(r)
    s.send("ERROR!\n".encode())
s.close()
