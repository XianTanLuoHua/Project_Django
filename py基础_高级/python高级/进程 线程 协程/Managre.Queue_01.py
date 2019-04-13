from multiprocessing import Manager,Pool
import os,time,sys
def reader(q):
    print('reader启动{0},父进程为{1}'.format(os.getpgid(),os.getppid()))
    for i in range(q.qsize()):
        print('reader从queue获取到消息:{0}'.format(q.get(True)))


def writer(q):
    print('writer启动{0},父进程为{1}'.format(os.getpid(),os.getppid()))
    for i in 'fongge':
        q.put(i)


if __name__ == '__main__':
    print('{0}启动'.format(os.getpid))
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer,(q,))
    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print('')