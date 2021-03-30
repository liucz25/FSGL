# Written by Vamei
# Client side
# 指定端口测试
import socket
 
# Address
sHOST = '127.0.0.1'
sPORT = 8080
cHOST = '192.168.2.103'
cPORT = 8000
request = 'GET  can you hear me?'
 
# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((cHOST,cPORT))
s.connect((sHOST, sPORT))
 
# send message
s.sendall(request.encode())
# receive message
reply   = s.recv(1024)
print ('reply is: ',reply)
# close connection
s.close()
