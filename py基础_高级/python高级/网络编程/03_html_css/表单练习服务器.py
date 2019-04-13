"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 表单练习服务器.py
@time: 19-3-25 下午4:50
"""
import socket
from urllib import *
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    server_socket.bind(('',8800))
    server_socket.listen(128)
    while True:

        client_socket,ip_port=server_socket.accept()

        client_message = client_socket.recv(1024)
        print(client_message.decode())

        line = 'http/1.1 200 ok\r\n'
        head = 'content-type:text/03_html_css;charset=utf-8\r\n'
        spc= '\r\n'
        body="访问成功"

        send_to =line+head+spc+body
        client_socket.send(send_to.encode())
        client_socket.close()


if __name__ == "__main__":
    main()
