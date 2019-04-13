"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: tcp客户端.py
@time: 19-3-20 下午4:12
"""
import socket
import time


def main():
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# 创建一个套接字对象使用ipv4协议
    tcp_client.connect(('192.168.27.68',8080))#使客户端连接到服务端

    # client_message = '你好吗'.encode('UTF-8')   # 发送字符串前进行解码
    tcp_client.send('你好吗'.encode('UTF-8'))     #发送

    recv_message = tcp_client.recv(1024)       #设置一个客户端入口进行接收并且阻塞,接收到信息解除阻塞,设置接收的最大字节数为1024
    recv_de_message = recv_message.decode('UTF-8')  #对接收的信息进行解码
    print('接收到服务端的信息',recv_de_message)      #打印接收的信息



    tcp_client.close()
if __name__ == "__main__":

    main()
