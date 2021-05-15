# !/usr/bin/python
import socket
import sys
import threading


# 上面的代码中还有一些小的方法没有定义：
# 由于是TCP代理，所以接收的信息块可能比较大，所以不直接用.recv()方法，而是写一个receive_from方法来获取发送的全部信息
def receive_from(connection):
    buffer = ""
    # 设置一个超时时间，如果超过2s没有接收到消息则进入异常处理（必须设置,如果不设置超时时间，则会阻塞，直到接收到消息为止，在本例中也许不会出现问题，但是如果客户端也需要发送请求时就会出现问题）
    connection.settimeout(0.1)
    try:
        # 将收到的消息拼接成buffer
        while True:
            data = connection.recv(4096)
            if not data:
                break
            print(data.decode())
            buffer += data.decode()
            print(buffer)
    # 如果2s都没收到消息，就返回空的buffer
    except:
        pass
    return buffer


# 对接收信息进行处理的函数，如果不需要特殊处理，直接返回收到的信息即可
def request_handler(buffer):
    # 此处添加具体的处理代码
    return buffer


def response_handler(buffer):
    # 此处添加具体的处理代码
    return buffer




def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    # 创建一个socket以连接服务端
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))
    # 如果需要服务端先向客户端发送信息
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        print("[<==]Receive %d bytes from remote host receive first" % len(remote_buffer))

        # 下面两行是对收到信息的处理，得到有用的信息（做十六进制处理和自定义的处理，如果不需要，可以省略）
        # hexdump(remote_buffer)
        remote_buffer = response_handler(remote_buffer)
        # 如果处理后仍有有用的信息，则发送给客户端
        if len(remote_buffer):
            client_socket.send(remote_buffer.encode())
            print("[==>]Sending %d bytes to local hosts" % len(remote_buffer))

    while True:

        remote_buffer = receive_from(remote_socket)
        print(remote_buffer)
        print("[<==]Receive %d bytes from remote host receive " % len(remote_buffer))

        # 下面两行是对收到信息的处理，得到有用的信息（做十六进制处理和自定义的处理，如果不需要，可以省略）
        # hexdump(remote_buffer)
        remote_buffer = response_handler(remote_buffer)
        # 如果处理后仍有有用的信息，则发送给客户端
        if len(remote_buffer):
            client_socket.send(remote_buffer.encode())
            print( "[==>]Sending %d bytes to local hosts" % len(remote_buffer))






        client_buffer = receive_from(client_socket)
        print(client_buffer)
        print("[<==]Receive %d bytes from client host receive " % len(client_buffer))

        # 下面两行是对收到信息的处理，得到有用的信息（做十六进制处理和自定义的处理，如果不需要，可以省略）
        # hexdump(remote_buffer)
        # remote_buffer = response_handler(remote_buffer)
        # 如果处理后仍有有用的信息，则发送给客户端
        if len(client_buffer):
            remote_socket.send(client_buffer.encode())
            print( "[==>]Sending %d bytes to remote hosts" % len(client_buffer))



# 定义上面的server_loop函数
def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    # 创建一个TCP socket以监听客户端
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except:
        print("Failed to listen on %s: %d" % (local_host, local_port), "Please try other socket")
        assert False

    server.listen(5)
    # 开始监听后，等待来自客户端的连接
    while True:
        print("waiting for local client connection")

        client_socket, addr = server.accept()
        print("[*]Received connection from %s:%d" % (addr[0], addr[1]))

        # 收到来自客户端的链接后，就开启一个代理线程
        proxy_thread = threading.Thread(target=proxy_handler,
                                        args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()

    # 定义代理线程





# 主函数：
def main():
    # 简单地判断命令格式，如果参数个数不是5个则提示正确的格式
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receivefirst]")

        exit(0)
    # 为监听客户端创建的socket
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    # 为连接服务端创建的socket
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    # 连接建立后是否由服务端先向客户端发送信息，True代表是
    if sys.argv[5] == "True":
        receive_first = True
    else:
        receive_first = False
    # 开始代理过程
    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


if __name__=='__main__':
    main()