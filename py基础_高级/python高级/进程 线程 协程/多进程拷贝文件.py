from multiprocessing import Pool,Manager
import os

def copy_old(name,queue):
    #完成拷贝一个文件的功能
    fr = open(r'C:\Users\84931\Desktop\old_files\{0}'.format(name),'r')
    fw = open(r'C:\Users\84931\Desktop\new_files\附件{0}'.format(name),'w')
    fw.write(fr.read())     #fw写入的就是fr读出来的
    fr.close()
    fw.close()
    queue.put(name)   #每次成功赋值都把从上层for循环得到的名字就传出去  被外界get捕获

def main():
    old_file_list = os.listdir(r'C:\Users\84931\Desktop\old_files')  #获取到 被拷贝的 文件夹中的文件名字 形成一个列表
    p = Pool(4) #进程池中的数量为4
    queue = Manager().Queue()  #实例一个队列
    for i in old_file_list:
        p.apply_async(copy_old,args=(i,queue))   #添加任务到进程池 并把队列当做参数传入进去 进行内部数据交互

#  打印目前copy的百分比进度
    num = 0 #初始化进度为0
    all_num = len(old_file_list) #获取文件的数量
    while True:
        queue.get()
        num +=1     #每次get一次数据就+=1  进行一次累计
        bt = num/all_num
        print('\r正在copy,进度{:0.2f}%'.format(bt*100),end='')

if __name__ == '__main__':
    main()