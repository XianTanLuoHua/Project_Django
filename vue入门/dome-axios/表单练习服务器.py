"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 表单练习服务器.py
@time: 19-3-25 下午4:50
"""
import socket
from urllib import *

import re
import fanyi


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('127.0.0.1', 8800))
    server_socket.listen(128)
    while True:

        client_socket, ip_port = server_socket.accept()
        client_message = client_socket.recv(1024)
        print('________')
        print(client_message.decode(),'++++++++++++++++++++++++++')
        print('________')
        p1 = re.compile(r'kw=\w+')
        a = p1.findall(client_message.decode())
        meg = a[0].split('=')[1]  # 对ajax请求发送的数据进行抽取得到value

        print('meg的类型:', type(meg))
        print('meg的数据:', meg)

        msg = fanyi.ipt(meg)  # 调用百度翻译 获取翻译后的结果
        print('msg的类型:', type(msg))

        a = ''  # 对得到的翻译后的结果进行拼接
        for i in msg:
            a = a + i['v']+'<br>'
        print(a)
        print(type(a))

        line = 'http/1.1 200 ok\r\n'
        head1 = 'content-type:text/html;charset=utf-8\r\n'
        head2 = 'Access-Control-Allow-Origin:*\r\n'
        spc = '\r\n'
        body = '{"k":'+r'"'+a+r'"'+'}'

        print(body)
        print(type(body))

        send_to = line + head1 + head2 + spc + body
        client_socket.send(send_to.encode('utf-8'))
        client_socket.close()


if __name__ == "__main__":
    main()
