"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: OOP_Web_server命令行传参修改端口号.py
@time: 19-3-25 上午9:25
"""
import socket
import threading
import time


def message_func(data):
    send_line ='http/1.1 200 OK\r\n'
    send_head = 'content-type:text/03_html_css;charset=utf-8\r\n'

    #根据客户端请求的地址进行不同的处理
    if data =='/index.03_html_css':
        send_body='index______show'
    elif data == '/login.03_html_css':
        with open('test.03_html_css','r')as f:
            send_body=f.read()
    else:
        send_line= 'http/1.1 403 NotFound\r\n'
        send_body='NOT</br>FOUND'

    return send_line,send_head,send_body




class mate_server():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(("", 8080))
        self.sock.listen(128)

    def func1(self, client):
            #接收客户端发来的消息并进行解码
            de_re = client.recv(1024)
            cli_message = de_re.decode('UTF-8')

            if cli_message:

                #对接收到的信息进行分割
                cli_message_sp = cli_message.split(' ')

                try:
                    #提取客户端请求的地址
                    #对没填写地址的请求进行处理,使其默认请求index文件
                    cli_message_sp_li = cli_message_sp[1]
                    if cli_message_sp_li =='/':
                        cli_message_sp_li = '/index.03_html_css'
                except Exception as e:
                    print('捕捉到请求的地址有异常', e)
                    client.close()
                    return


                #处理html请求,通过封装函数得到处理过的行头体
                if cli_message_sp_li.endswith('.03_html_css'):
                    send_spc = '\r\n'
                    send_line,send_head,send_body = message_func(cli_message_sp_li)
                    send_message =send_line+send_head+send_spc+send_body
                    client.send(send_message.encode('UTF-8'))

                #处理非html请求
                else:

                    try:
                        #如果打开文件路径正确就不会报错正确执行
                        with open('./{0}'.format(cli_message_sp_li),'rb')as f:
                            send_body=f.read()
                            send_line = 'http/1.1 200 OK\r\n'
                            send_head = ''
                            send_spc = '\r\n'
                            send_to_img = send_line.encode('UTF-8')+send_head.encode('UTF-8')+send_spc.encode('UTF-8')
                            client.send(send_to_img+send_body)

                    except:
                        #如果不存在文件捕捉异常
                        send_line,send_head,send_body = message_func(None)
                        send_spc = '\r\n'
                        send_message=send_line+send_head+send_spc+send_body
                        client.send(send_message.encode('UTF-8'))

                client.close()
            else:
                client.close()
                return

    def run(self):
        while True:

            #循环接受客户端发来的连接
            client, cli_ip_port = self.sock.accept()


            thread_client = threading.Thread(target=self.func1, args=(client,),daemon=True)
            thread_client.start()
            time.sleep(1)
            print('a')


def main():
    #实例化一个对象
    cli = mate_server()

    #启动
    cli.run()

if __name__ == "__main__":
    main()
