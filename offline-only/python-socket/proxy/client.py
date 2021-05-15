# !/usr/bin/python
import sys
import socket


def receive_from(connection):
    buffer = ""
    connection.settimeout(0.01)
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

