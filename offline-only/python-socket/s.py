import socket
HOST='127.0.0.1'
PORT=5000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(128)

r='''HTTP/1.x 200 OK  
Content-Type: text/html

<html>
<head>
<title>WOW</title>
</head>
<p>Wow, Python Server</p>

</html>
'''

while 1:
    conn,addr=s.accept()
    print("connect by ",conn)
    while 1:
        data=conn.recv(1024)
        if data:
            print("data:",data)
            conn.sendall(r.encode())
        else:
            break
    conn.close()

s.close()
