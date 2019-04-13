from threading import Thread
import time

g_num = 100

def func_1():
    global g_num
    for i in range(5): #每次循环过后进行加一 循环五次
        g_num+=1


def func_2():
    global g_num
    print('现在全局变量{0}被修改成了{1}'.format("g_num",g_num))



print('线程创建之前g_num的值为{0}'.format(g_num))
f1 = Thread(target=func_1)
f1.start()

time.sleep(1)  #阻塞1s后 再执行func2看看全局变量是否被修改

f2 = Thread(target=func_2)
f2.start()

