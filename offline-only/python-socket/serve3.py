
import socket
import struct
 
# Address
HOST = ''
PORT = 8080
 
# Prepare HTTP response
text_content = '''HTTP/1.x 200 OK  
Content-Type: text/html

<html>
<head>
<title>WOW</title>
</head>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''


# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
 
# Read picture, put into HTTP format
f = open('test.jpg','rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic =  pic_content.encode()+ f.read()
f.close()
# Read picture, put into HTTP format
f2 = open('favicon.ico','rb')
p2_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
p2 =  p2_content.encode() + f2.read()
# p2=f2.read()
f2.close()
 
# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
 
# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request    = conn.recv(1024)
    # print(request.decode().split(' ')[1])
    method     = request.decode().split(' ')[0]
    
    src        = request.decode().split(' ')[1]
    print(method)
    # deal with GET method
    if method == 'GET':
        # ULR    
        # print(type(pic))
        if src == '/test.jpg':
            content = pic
        elif src == '/favicon.ico':
            # print(type(p2))
            content=p2
        else: content = text_content.encode()
 
        print ('Connected by', addr)
        # print ('Request is:', request)
        conn.sendall(content)
    # close connection
    conn.close()
