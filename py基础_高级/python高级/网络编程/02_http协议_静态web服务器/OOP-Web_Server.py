"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: OOP-Web_Server.py
@time: 19-3-23 下午2:28
"""
import socket
import threading

from python高级.网络编程.http协议_静态web服务器 import web_mode


class meta_server():
    def __init__(self):

        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        ip_port = ("", 8080)
        self.socket_obj.bind(ip_port)
        self.socket_obj.listen(128)

    def func_server(self, client):
        client_message = client.recv(1024)

        # 判断请求是否为空数据
        if client_message:
            # 抽取路径
            client_data = client_message.decode('UTF-8')
            print(client_data)
            client_data_split = client_data.split(' ')
            print(client_data_split)
            # 判断路径 且给一个/ 补充为默认的/index.thml
            try:
                file_path = client_data_split[1]
                if file_path == '/':
                    file_path = '/index.03_html_css'

            except Exception as e:
                client.close()
                return

            # 判断请求资源的格式
            if file_path.endswith('.03_html_css'):

                #如果找到了文件的逻辑处理 通过封装的函数得到 行 头 体
                send_line, send_head, send_body = web_mode.main(file_path)
                send_spc = '\r\n'
                send_to_cli = send_line + send_head + send_spc + send_body
                client.send(send_to_cli.encode('utf-8'))

            # 处理所有 非.html的请求
            else:
                # 如果找到了文件
                try:
                    with open('./{0}'.format(file_path), 'rb')as f:
                        send_body_img = f.read()
                    send_line_img = 'http/1.1 200 OK\r\n'
                    send_head_img = ''
                    send_spc_img = '\r\n'
                    send_to_cli = send_line_img.encode('UTF-8') + send_head_img.encode('UTF-8') + send_spc_img.encode(
                        'UTF-8') + send_body_img
                    client.send(send_to_cli)


                # 未找到文件404
                except:
                    send_line_img = 'http/1.1 403 NotFound!\r\n'
                    send_head_img = 'content-type:text/03_html_css;charset=utf-8;\r\n'
                    send_spc_img = '\r\n'
                    send_body_img = '您输入的地址有误</br>请重新输入'
                    send_to_cli = send_line_img + send_head_img + send_spc_img + send_body_img
                    client.send(send_to_cli.encode('UTF-8'))

            client.close()

        else:
            client.close()
            return

    def server_run(self):
        while True:
            # 循环接收并且调用具体功能代码
            client_accept, addrs = self.socket_obj.accept()
            threading.Thread(target=self.func_server,args=(client_accept,)).start()

def main():
    client_server_01 = meta_server()
    client_server_01.server_run()

if __name__ == "__main__":
    main()
