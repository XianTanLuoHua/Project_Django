import threading
import time

# '''
#         下面这段代码,主进程结束后 子线程依然会继续运行
# '''
# def func_1():
#     print('我开始了')
#     time.sleep(3)
#     print('我结束了')
#
# f1 = threading.Thread(target=func_1,args=())
# f1.start()
# time.sleep(1)
# print('主进程结束了哦')


'''
        试着加入daemon  子线程和主进程一起终止
        设置方法:二选一
            f2.setDaemon(True)
            f2.daemon = True
'''

def func_2():
    print('我是守护线程 我开始了')
    time.sleep(3)
    print('我是守护线程我结束了')  #并不会出现 因为主进程结束了 此进程自动终止

f2 = threading.Thread(target=func_2,args=())
f2.setDaemon(True )
# f2.daemon=True

f2.start()

time.sleep(1)
print('我是主进程我结束了')







