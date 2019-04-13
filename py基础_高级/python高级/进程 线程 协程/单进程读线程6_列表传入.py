import threading
import time

a = [1,2,3,4]

def func_1(lst):
    print('func_1接收到一个可变类型list{0}'.format(lst))
    lst.append(5)
    print('func_1增加一个元素5到列表中')


def func_2(lst):

    time.sleep(1)   # 停顿一秒来让func_1有时间执行
    print('func_2接收到一个全局变量数据',lst)



f1 = threading.Thread(target=func_1,args=(a,))
f1.start()


f2 = threading.Thread(target=func_2,args=(a,))
f2.start()