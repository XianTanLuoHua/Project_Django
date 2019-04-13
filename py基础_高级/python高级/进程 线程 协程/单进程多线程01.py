import threading
import time


def func_1(name):
    print('我叫{0}现在{1},我开始了'.format(name, time.ctime()))
    time.sleep(2)
    print('我叫{0}现在{1},我休息了2s 我结束了'.format(name, time.ctime()))


def func_2(name, age):
    print('我叫{0},今年{1},现在{2}我开始了'.format(name, age, time.ctime()))
    time.sleep(4)
    print('我叫{0},今年{1},现在{2}我休息了4s 我结束了'.format(name, age, time.ctime()))


def main():
    print('开始下发任务')
    f1 = threading.Thread(target=func_1,args=('小明',))
    f1.start()

    f2 = threading.Thread(target=func_2,args=('花花', 20))
    f2.start()

    print('主线程任务完成')


if __name__ == '__main__':
    main()
    print('这里主程序继续往下执行 不等子线程结束')
