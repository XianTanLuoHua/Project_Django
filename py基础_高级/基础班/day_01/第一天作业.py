
a = input('请输入一个数字来')
b = eval(a)
print('您输入的数字是%d' %b)



c = eval(a[::-1])

print('反转后就是%d'% c)




# '''
# 一个很low的方法
# '''
#
# a = input('请输入你想的数字')
# x = len(a)
# d = 0
# for i in a:
#     b = ord(i)
#     x -= 1
#     c = (b-48)*(10**x)
#     d +=c
#
# print(d)
# print('*'*20)
#
#
#
# a = list(input('请输入数字我给您反转一下'))
# a.reverse()
# x = len(a)
# d = 0
# for i in a:
#     b = ord(i)
#     x -= 1
#     c = (b-48)*(10**x)
#     d +=c
#
# print(d)
# print(type(d))







