"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: tcp服务端.py
@time: 19-3-20 上午11:51
"""

import socket
import time


def main():
    sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # 1.创建服务端套接字实例 AF_INET 代表ipv4协议
    sock_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)     # 并让其端口程序退出后端口立即释放

    sock_.bind(('192.168.27.68', 8080))  # 2.绑定ip与端口 ip为空则为当前网卡ip

    sock_.listen(128)  # 3.设置服务端被动监听与最大连接数


    server_, ip_post = sock_.accept()  # 4.阻塞执行等待接收客户端的连接请求,与客户端连接成功才会结束阻塞,代码向下执行
                                   #  accept 会返回两个元素:1.专门和客户端通讯的sorcket对象,2.包含客户端的ip与端口

    print('到这一步表示已经连接成功,我们看一下客户端的ip与端口号', ip_post)

    recv_data = server_.recv(1024)  # 5.recv 接收客户端内的信息并设置接受的信息最大为1024字节

    recv_message = recv_data.decode('UTF-8')   #6. 对信息进行解码

    print('接收到客户端的信息',recv_message) #7.对接收到的信息进行打印


    send_message = recv_message.replace('吗','')
    send_message = send_message.replace('?','!')
    server_.send('{0}!'.format(send_message).encode('UTF-8'))

    server_.close()
    sock_.close()

if __name__ == "__main__":
    while True:

        main()
