import socket as sk

s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.bind('',12345)

s.listen(1)
sock,addr = s.accept()

a = sock.recv(1024).decode()

a = open(a,'rb')

s.send(a.read())
s.send("!#end\n".encode)

print(s.recv(1024).decode())
s.close()
a.close()
exit(0)
