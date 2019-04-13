'''
        eval(str)  计算在字符串中的有效Python表达式,并返回一个对象
'''
a = '1+2'
print(a)
print(type(a))
a = eval('1+2')
print(a)
print(type(a))

print('*'*20)

'''
        repr(x )	将对象 x 转换为表达式字符串
'''
a = 1+1
print(a)
print(type(a))
a = repr(1+1)
print(a)
print(type(a))

'''
        chr输入int类型 得到的是字符串    根据输入的数字从ascii码表按照索引找到value并 return
        ord 输入str类型将字符转换为数字   return回来ascii码表上该字符的索引号
'''
print(chr(97))  #根据ascii码表上的索引是a
print(ord('a')) #将字符串转成ascii码表上的索引号

print(chr(98))
