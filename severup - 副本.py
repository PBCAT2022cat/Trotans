from socket import *
import sys

path = input('my path:')
names = input('name:')

s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.0.105',12345))
s.listen(1)
sock,addr = s.accept()

sock.send((names+'\n').encode())
with open(path,'rb') as file:
    lens = sys.getsizeof(file.read())
sock.send((str(lens)+'\n').encode())
cout = sock.recv(1024).decode().rstrip()
if cout == "good":
    with open(path,'rb') as file:
        sock.send(file.read())
    cout = sock.recv(1024).decode().rstrip()
    print(cout)
else:
    print('ERROR')

s.close()
sock.close()
