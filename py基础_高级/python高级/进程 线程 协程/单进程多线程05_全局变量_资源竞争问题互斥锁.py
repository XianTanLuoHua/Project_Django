"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 单进程多线程05_全局变量_资源竞争问题互斥锁.py
@time: 19-3-19 下午2:48
"""

import threading
import time

lk = threading.Lock()

num = 0


def func1():
    global num

    for i in range(1000000):
        lk.acquire()
        num += 1
        lk.release()


def func2():
    global num

    for i in range(1000000):
        lk.acquire()
        num += 1
        lk.release()


def main():
    t1 = time.time()
    f1 = threading.Thread(target=func1)
    f2 = threading.Thread(target=func2)
    f1.start()
    f2.start()

    f1.join()
    f2.join()
    t2 = time.time()
    print('加锁用时:',t2 - t1)



if __name__ == "__main__":
    main()

    t3 = time.time()
    num_a = 0
    for i in range(2000000):
        num_a += 1
    t4 = time.time()
    print('不加用时:', t4 - t3)
