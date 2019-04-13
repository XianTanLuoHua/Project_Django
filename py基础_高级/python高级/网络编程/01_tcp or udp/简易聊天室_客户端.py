"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 简易聊天室_客户端.py
@time: 19-3-20 下午7:33
"""
import socket
import time


def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    send_to = ('127.0.0.1',8080)
    client.connect(send_to)
    while True:

        want_str = input('您想发送什么?')
        client.send(want_str.encode('UTF-8'))
        # time.sleep(0.1)
        client.send('隔了0.1秒了'.encode('UTF-8'))
        accept_server_recv = client.recv(1024)

        if want_str == 'exit':
            client.close()
            break

        print(accept_server_recv.decode('UTF-8'))

if __name__ == "__main__":
    main()
