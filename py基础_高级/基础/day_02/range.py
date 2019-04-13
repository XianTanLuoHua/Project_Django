'''
        range(start stop,步长)看左不看右  如果不设置默认为0 步长默认为1
'''
a = []
for i in range(0,100,2):

    a.append(i)
print(a)     #默认从0开始 以stop-1 结束
print('*'*20)

a = []
for i in range(1,10):
    a.append(i)
print(a)     #给出start参数 从start开始
