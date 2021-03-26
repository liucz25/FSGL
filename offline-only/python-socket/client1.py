# Written by Vamei
# Client side
import socket
 
# Address
HOST = '192.168.2.102'
PORT = 8000
 
request = 'can you hear me?'
 
# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
 
# send message
s.sendall(request.encode())
# receive message
reply   = s.recv(1024)
print ('reply is: ',reply)
# close connection
s.close()
