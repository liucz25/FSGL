import socket


HOST=''
PORT=8000

reply='Yes'

#config socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.socket()创建一个socket对象，并说明socket使用的是IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)。
s.bind((HOST,PORT))

s.listen(3)  #3最大连接队列数，最多同时连接3台客户端
conn,addr=s.accept()
req=conn.recv(1024)
print ('request is: ',req)
print ('Connected by', addr)
conn.sendall(reply.encode())

conn.close()