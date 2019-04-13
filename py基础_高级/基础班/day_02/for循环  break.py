'''
        for循环 是一个闭包环境    for中的else和循环是一个整体
'''
i = '哈哈'
for i in range(10):
    print(i)
print(i)
print('*'*20)

'''
        正常循环中 如果没有break语句 else 会作为结尾执行
'''
for i in range(10):
    if i == 7:
        print('我是7需要终止运行')
    print(i)
else:
    print('over')

print('*'*20)


'''
 碰到break  终止整个循环
'''
for i in range(10):
    if i == 7:
        print('我是7需要终止运行')
        break
    print(i)
else:
    print('over')