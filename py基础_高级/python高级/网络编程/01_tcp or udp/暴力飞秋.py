import socket
# from multiprocessing import Pool
# def func1():
#     while True:
#         for i in range(255):
#             udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             udp_socket.sendto('1:525:隔壁老王:隔壁老王:32:Hello Python\n好好学习天天向上'.encode('gbk'), (r'192.168.27.{0}'.format(i), 2425))
# if __name__ == '__main__':
#     p = Pool(6)
#     for i in range(6):
#         p.apply_async(func1,args=())
#     p.close()
#     p.join()

import socket
from multiprocessing import Pool
def func1():
    while True:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto('1:525:隔壁老王:隔壁老王:32:Hello Python\n好好学习天天向上'.encode('gbk'), (r'192.168.27.xxx', 2425))
if __name__ == '__main__':
    p = Pool(6)
    for i in range(6):
        p.apply_async(func1,args=())
    p.close()
    p.join()

# for i in range(3,256):
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.sendto('1:525:阳光男孩:阳光男孩:32:{0}'.format(a).encode('gbk'), (r'192.168.27.{0}'.format(i), 2425))





