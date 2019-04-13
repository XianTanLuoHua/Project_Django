import threading
import time


g_num = 0


def func_1():
    global g_num
    for i in range(1000000):
        g_num+=1
    print('\rfunc1中的for循环了100w次得到的是{0}'.format(g_num))


def func_2():
    time.sleep(1)  #可以看到这句话如果不注释掉 每次运行的结果都不一样,因为两个线程在争抢资源
    global g_num
    for i in range(1000000):
        g_num+=1
    print('\rfunc2中的for循环了100w次得到的是{0}'.format(g_num))



f1 = threading.Thread(target=func_1)
f1.start()



f2 = threading.Thread(target=func_2)
f2.start()


f2.join()
print('都加减完毕目前全局变量修改成了{0}'.format(g_num))