i = 1
while i <= 5:  #外层循环控制行
    c = 1
    while c <=5: #内层循环控制列
        print('*',end=' ') #print默认末尾带end'\n'  改变默认 每次循坏打印的时候加一个空格
        c+=1
    i+=1
    print()
print('*'*20)
'''
        倒三角形
'''
i = 1
while i<=5:
    c = i
    while c <=5:
        print('*', end=' ')  # print默认末尾带end'\n'  改变默认 每次循坏打印的时候加一个空格
        c += 1
    i += 1
    print()

print('*'*20)
'''
        正三角形
'''

i = 1
while i <=5:
    c = 1
    while c<=i:
        print('*',end=' ')
        c+=1
    i+=1
    print()



