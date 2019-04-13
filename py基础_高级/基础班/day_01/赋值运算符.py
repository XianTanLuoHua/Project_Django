'''
数值调换
'''
a = 1
b = 2
print(a,b)
a,b = b,a
print(a,b)
print('*'*20)


'''
注意赋值运算符右边优先级最高
'''
a = 10
a *= 2+3
print(a)
print('*'*20)


'''
沙雕代码
'''
# a = 2
# b = 3
# # a+=(b*=3) #这是一段沙雕代码
# print(a)