'''
        for
'''
for i in range(1,10): # 外层循坏控制行
    for a in range(1,i+1): # 内层循环控制列  内层循环的终止 随着外层变量控制
        print('{0}*{1}={2}'.format(i,a,i*a),end='\t')
    print('')
print('*'*20)
'''
        for and while
'''
for i in range(1,10):
    a = 1
    while a <= i:
        print("%d*%d=%-2d"%(a,i,a*i),end=" ")
        a +=1
    print()

print('*'*20)
''' 
        while
'''
i = 1
while i <= 9:
    c = i
    while c <=9:
        print('{0}*{1}={2}'.format(i,c,c*i),end='\t') #使用制表符对齐
        c+=1
    i +=1
    print()
print('*'*20)
i = 1
while i <= 9:
    c = 1
    while c <=i:
        print('{0}*{1}={2: <3}'.format(c,i,c*i),end='') #使用格式化对齐
        c+=1
    i +=1
    print()