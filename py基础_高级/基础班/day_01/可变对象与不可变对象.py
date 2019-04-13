'''
可变对象与不可变对象
'''
a = [12]
b = a
print(id(a))
print(id(b))

print(a)
print(b)
a.append(11) #只修改a 但是b也会改变
print(a)
print(b)
print(id(a))
print(id(b))

print('*'*20)

a = 1
b = a
print(a,b)
print(id(a),id(b))
a = '小明' #a重新指向了一块新的内存
print(a,b)
print(id(a),id(b))

