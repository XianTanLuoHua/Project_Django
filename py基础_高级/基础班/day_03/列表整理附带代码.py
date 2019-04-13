

'''
        用for循环list 时  会在内存中复制出来一份列表出来 形成闭包
'''
c_list = [1,2,3,4]
for i in c_list:
    print(i)
    i = i*10
    c_list = i*10 #这里虽然每次循环都给本体赋值 但是并不改变整体循环 因为for循环的是提前赋值的封闭环境
print(c_list)    #这里输出400 说明外部已经被改变了


'''
        list.pop(index)   如果不给index参数 默认弹出最后一个参数 弹出可以用一个变量接收
        del list[index]   删除索引位置的元素  del listName 删除整个对象
        list.remove(obj)  指定list层匹配(默认第一层) 删除指定obj 如果存在多个 只删除第一个
        list.clear() 清空
'''
c_list = [1,2,3,4,'a']
for i in range(len(c_list)):
    c_list.pop(0)
print(c_list)

print('*'*20)
c_list = [1,2,3,4,'a']
for i in range(len(c_list)):
    del c_list[0]
print(c_list)

print('*'*20)
c_list = [1,2,3,4,'a']
c_list.remove('a')
print(c_list)

print('*'*20)
c_list = [1,2,3,4,'a']
c_list.clear()
print(c_list)



print('*'*20)
'''
        list.sort(key=None,reverse=Flase) 使self根据ascii码表进行排序  如果有参数则按照参数设置
        list.reverse(self) 使self中元素逆转
        sorted(list) sorted() 函数对所有可迭代的对象进行排序操作。
'''
a = ['3','1','a','2','b']
b = sorted(a)  #使用b来接收return的参数
print(a)
print(b)
print('*'*20)
a = ['3','1','a','2','b']
a.sort()
print(a)
a.sort(reverse=True) # 默认Flase 设置True参数后会进行排序后并逆转
print(a)
print('*'*20)
a = ['3','1','a','2','b']
print(a)
a.reverse() #单纯的逆转
print(a)
print('*'*20)
a = ['3','1','a','2','b']
b = sorted(a) #需要一个变量来接收返回值
print(b)
print('*'*20)
a = [[1,3],[3,7],[2,5]]
k = lambda x:x[1]
a.sort(key=k)
print(a) # 排序时按照索引为1的值进行排


print('*'*20)
'''
        list.append(obj) 在list内末尾添加指定元素
        list_1.extend(iterable_obj) 在末尾追加一个iterable的对象
        list.insert(index,obj) 在索引位置插入一个obj如果超出索引会默认添加到最后
'''
a = [1,2,3]
b = ['a','b']
a.append(4) #在末尾添加新元素4
print(a)
a.extend(b) #在末尾追加一个可迭代对象
print(a)
a.insert(1,'haha') #在下标为1的地方插入'haha'
print(a)
a.insert(100,'没有第一百位啊')#就默认插在最后面
print(a)



'''
        list.index(self,obj,start,end) 查找如果找不到会报错,start默认0 end默认结尾开始查找,return索引
        list.count(self,obj)统计obj出现在list中的次数 return回count值
        in              obj in iterable_obj   返回bool值
        not in          obj not in iterable_obj 返回bool值
'''
a = [2,1, 'haha', 2, 3, 4, 'a', 'b', '没有第一百位啊']
print(a.index('haha'))
print(a.count(2))


'''
        copy  只复制最外层的关系链
'''