import threading
import time


def func_1():
    print('我是func1 方法一要执行了')
    time.sleep(3)
    print('休眠了3s 方法一结束了')

def func_2():
    print('我是func2 方法二要执行了')
    time.sleep(5)
    print('休眠了6s 方法二结束了')

def func_3():
    print('我是func2 方法三要执行了')
    time.sleep(1)
    print('休眠了1s 方法三结束了')

def main():
    print('main开始运行了{0}'.format(time.ctime()))
    f1 = threading.Thread(target=func_1,args=())
    f2 = threading.Thread(target=func_2,args=())
    f3 = threading.Thread(target=func_3,args=())
    f1.setName('fun1')
    f2.setName('fun2')
    f3.setName('fun3')
    f1.start()
    f2.start()
    f3.start()
    time.sleep(2)
    for thr in threading.enumerate():
        print('正在运行的线程名字是{0}'.format(thr))
    print('正在运行的线程数量是{0}'.format(threading.activeCount()))
    print('main结束了{0}'.format(time.ctime()))
if __name__ == '__main__':
    main()

