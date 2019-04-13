import time
import threading
class the(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = '我是{0} 目前抽到了{1}\n'.format(self.name,i)
            print(msg)

def main():
    for c in range(5):
        t = the()
        t.start()
if __name__ == '__main__':
    main()


'''
        实例化的t然后start后会自动执行the(threading.Thread)中的run方法,
        test()中的 for c in xxx  意味着开了五个线程来执行run中的代码
        后由系统调度线程的执行顺序
        self.name 可以获取到当前的线程的名字
'''