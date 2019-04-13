"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 简易聊天室_服务端.py
@time: 19-3-20 下午7:13
"""

import socket

def main():
    server_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    server_.bind(('192.168.27.29',2330))
    server_.listen(128)
    server_cli,cli_ip_port = server_.accept()
    print(cli_ip_port,'已经连接')
    while True:

        server_cli_message = server_cli.recv(1024)

        print('接收到客户端发送的消息',server_cli_message.decode('UTF-8'))


if __name__ == "__main__":
    main()
