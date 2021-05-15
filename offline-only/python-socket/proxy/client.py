# !/usr/bin/python
import sys
import socket


def receive_from(connection):
    buffer = ""
    connection.settimeout(0.1)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        # print "no data received !!!!"
        pass
    return buffer
def sendto(request_queue):
    # 如果有已建立的socket连接，则提示用户输入想要发送的信息内容
    if request_queue:
        msg = input("message:")
        # 如果用户输入的是"exit",就关闭所有的连接，否则就向所有已连接的客户端发送输入的内容
        if msg == "exit":
            for client_socket in request_queue:
                client_socket.close()
                break
        else:
            # 由于本例中只是简单地发送消息，所以直接用send方法，如果是比较耗时的操作，可以创建对每个request创建一个线程
            for client_socket in request_queue:
                client_socket.send(msg.encode())
                print("sending %s to proxy" % msg)


def main():
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        # data = receive_from(client)
        data=client.recv(1024)
        if data:
            print(data.decode())

if __name__ == '__main__':
    main()

