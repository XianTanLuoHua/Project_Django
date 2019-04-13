from multiprocessing import Queue
q = Queue(3)
q.put('消息2')
q.put('消息')
print(q.full(),'full 这里因为队列中只有一条消息 没有满载 所以返回False')
q.put('消息3')
print(q.full(),'full 这里队列因为前面的三条消息 所以队列满了 返回True')
print(q.empty(),'empty 队列里面还有消息 所以返回 False')
print(q.qsize(),'这里打印队列里面消息的数量')
q.get()    #取出来一条
print(q.qsize(),'这里因为以上面取出来了一条  所以打印2')
q.get_nowait()
q.get_nowait()
print(q.qsize(),'这里因为上面两个get_nowait取完了  所以为0')
# q.get()  #这里会等待有数据传输进来   如果没有则堵塞进程 下面的代码就无法执行
# q.get_nowait()  #这一句代码不等待数据传输进来  如果取不到数据 直接异常
q.put('消息1')
q.put('消息2')
q.put('消息3')
# q.put('消息4')
print(q.qsize(),'上面的消息如果不注释掉 就会造成堵塞 因为队列中的消息只能容纳一条   所以打印输出3')


# q.put_nowait('已经满了 这条命令不会阻塞 会报异常消息')
q.put('消息5')# 添加一下消息
print('这里不会执行是因为以上面的命令让这里堵塞了')

q.get()
print(q.qsize(),'测试1')


