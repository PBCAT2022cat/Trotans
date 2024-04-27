import socket,threading,sys
cmds=['upload','exit','use py']
print(*cmds)

def upload():
    try:
        path = input('my path:')
        names = input('name:')
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
    except Exception as rr:
        print(rr) 

def usePy():
    try:
        sock.send((input('name:')+'\n').encode())
        a = sock.recv(1024).decode().rstrip()
        print(a)
    except Exception as rr:
        print(rr)



def sendd():
    global hello,cmds
    try:
        a = input('cmd > ')+'\n'
        if a.rstrip() in cmds:
            sock.send('useModel------\n'.encode())
            if a == 'upload\n':
                sock.send(a.encode())
                upload()
            elif a == 'exit\n':
                sock.send(a.encode())
                hello = False
            elif a=='use py\n':
                sock.send(a.encode())
                usePy()
        else:
            sock.send(a.encode())
            num = sock.recv(1024).decode()
            num = int(num)
            num *= 8
            num += 2048
            a = sock.recv(num).decode()
            print(a)
        
    except Exception as rr:
        print(rr)

hello = True
print(socket.gethostname())
host = '0.0.0.0'
post = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#定义套接字（类型）
s.bind((host,post))#监听
s.listen(1)
sock,addr = s.accept()
try:
    while hello:
        sendd()
        
except Exception as r:
    print(r)
    
hello = False
s.close()
sock.close()
