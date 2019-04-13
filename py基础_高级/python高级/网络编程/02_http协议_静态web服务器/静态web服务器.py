"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 静态web服务器.py
@time: 19-3-22 下午2:52
"""
import socket
import threading
import time


def sever_func1(web_client_data):
    while True:
        try:

            # 接收客户端发来的信息
            client_message = web_client_data.recv(4096)
            if len(client_message)==0:
                print('客户端关闭了')
                web_client_data.close()


            else:

                # 对客户端发来的信息进行打印
                print(client_message.decode('UTF-8'))

                # 响应行
                send_message_line = 'HTTP/1.1 200 OK\r\n'
                # 响应头
                send_message_head1 = 'Server:web_test1.0\r\n'
                send_message_head2 = 'content-type:text/03_html_css;charset=utf-8;\r\n'
                # 响应体
                send_message_body = '月薪两万带带我'

                # 拼接要发送的字符串
                send_message = (send_message_line + send_message_head1 + send_message_head2 + "\r\n" + send_message_body).encode("UTF-8")

                # 对客户端进行回馈
                web_client_data.send(send_message)

        except:
            pass

        finally:
            #关闭与客户端的连接

            web_client_data.close() # 如果不关闭则浏览器一直等待一个完整的回话结束
            # break


def main():
    # 创建一个服务器端
    web_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    web_sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定服务器ip与端口
    web_sever.bind(('', 8080))

    # 设置监听
    web_sever.listen(8)

    # 循环接收连接
    while True:
        print('阻塞1')
        # 开始处理客户端发来连接请求
        web_client_data, web_client_ip_port = web_sever.accept()
        print('阻塞2')
        print('接收到:{0}的连接'.format(web_client_ip_port[0]))

        # #启用多任务处理客户端
        threading.Thread(target=sever_func1, args=(web_client_data,),daemon=True).start()
        # sever_func1(web_client_data)

if __name__ == "__main__":
    main()
