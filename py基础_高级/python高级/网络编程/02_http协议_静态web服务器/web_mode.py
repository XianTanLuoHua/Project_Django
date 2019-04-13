"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: web_mode.py
@time: 19-3-23 下午3:51
"""


def main(client_data):
    send_line = 'http/1.1 200 OK\r\n'
    send_head = 'content-type:text/03_html_css;charset=utf-8;\r\n'

    if client_data =='/index.03_html_css':
        send_body = 'index_______show'

    elif client_data == '/login.03_html_css':
        with open('./post.03_html_css','r')as f:
            send_body = f.read()

    else:
        send_line = 'http/1.1 404 NotFound\r\n'
        send_body = 'Not</br>Found'


    return send_line,send_head,send_body


if __name__ == "__main__":
    main()
