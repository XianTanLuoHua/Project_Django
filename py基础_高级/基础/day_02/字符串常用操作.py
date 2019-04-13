


'''
        字符串的操作不能改变对象本身  因为不可变
'''


'''
        切片 [起始:结束:步长]  起始默认为0 步长默认为1  如果是负数 就从右往左取
        切片 不取结束那一位  取左不取右
        切片不改变现有对象
'''
a = 'hello asdffAAgds1_2_3_4i'
b = '123'
c = 'ac'
d = '哈哈a1'

print(a[:]) # 取所有
print(a[:10:2]) # 从开始取到下标为10-1的位置  步长为2
print(a[-5:-1])# 从下标为-5 的地方取到-1-1的位置 步长为1x
print(a[8:1:-1]) # 从第八位的索引位置取值到1+1的位置 步长为-1
print(a[::-1])  #倒叙



print('*'*20)
'''
        obj.find(str) 查找索引  str.find(obj,start,end)
        如果没有找到return -1
        rfind   right从右边开始查找
'''
print(a.find('f'))
print(a.find('anb'))


print('*'*20)
'''
        index 查找索引    str.index(self,obj,start,end)
        如果没有 会报错    ValueError: substring not found
        rindex right从右边
'''
print(a.index('l'))


print('*'*20)
'''
        replace 替换   str.replace(old,new,num) return一个str 不改变现有对象
'''
a_replace =a.replace('a','A',1)
print(a_replace)


print('*'*20)
'''
        obj.count(str) 统计   str.count(obj,strat,end) 如不设置默认参数,即默认统计从开始到结尾该obj出现的次数
        return一个int对象
'''
print(a)
a_count=a.count('a')
print(a_count)


print('*'*20)
'''
        obj.split(str)  分割 分离   obj.split('str',maxsplit)
                        以obj中包含的str为分割线 用空字符替换分割  分割次数如不设置参数默认分割所有
                        如不设置str参数 默认以制表符分割
        return一个[]  字符串列表
'''
a_split = a.split()
print(a_split)
a_split = a.split('_')
print(a_split)


print('*'*20)
'''
        str.splitlines()  按照行分割 返回一个字符串列表
'''
f = '可惜不是你\n陪我到最后'
g = f.splitlines()
print(g)


print('*'*20)
'''
        obj.partition(str)  返回一个tuple 以str为分割线 只分割一次 左右分割 包含字符串本身
'''
i = 'hello word python'
p = i.partition('o')
print(p)
p = i.rpartition('o')
print(p)


print('*'*20)
'''
        in  判断字符是否在某个字符串内 return一个bool值
'''
print('a' in a)


print('*'*20)
'''
        obj.title()  把字符串每个单词首字母大写其他字符转换成小写 return回一个字符串
        分割符 以非英文字符作为分割符
'''
a_title = 'xiao ming5sui'
print(a_title.title())   #  以5还有空格 为分割符


print('*'*20)
'''
        obj.capitalize()  首字母大写    return回一个字符串
'''
a_capitalize = a.capitalize()
print(a)
print(a_capitalize)


print('*'*20)
'''
        obj.lower()    return一个全部小写的对象
        obj.upper()    return一个全部大写的对象
'''
a_lower = a.lower()
a_upper = a.upper()
print(a_lower)
print(a_upper)


print('*'*0)
'''
        obj.isalpha()  如果obj中全部都是字符串则return True
        obj.isdigit()  检测obj中是否全部为数字字符
        obj.isalnum()    alpha number的缩写 检测obj中是否只存字母或数字字符 如果有符号则return Flase
        obj.startswith(str) 判断obj是否以指定字符串开头
        obj.endswith(str)   判断obj是否以指定字符串结尾
        obj.islower() obj.isupper()  判断obj是否全部大小写
        obj.isspace()  判断obj是否存在制表符\t \n ' '
        obj.startwith(str) 检查字符串是否是以指定子字符串开头
        obj.endwith(str)
'''
print(a.isupper(),a)
print(b.isalpha(),b)
print(c.isalpha(),c)
print('*'*20)
print(a.isdigit(),a)
print(b.isdigit(),b)
print(c.isdigit(),c)
print('*'*20)
print(d.isalnum(),d)
s = 'www.baidu.com'
print(s.startswith('www'),s)
print(s.endswith('com'),s)


print('*'*20)
'''
        str.join(obj)   obj字符串序列中每个单词插入一个str,return一个新的字符串
'''
obj = ('haha','wo','ai')
obj1 = '小明是个小学生'
a = ''
b = '_'
print(a.join(obj))
print(b.join(obj))
print(b.join(obj1))


print('*'*20)
'''
        obj.strip()  删除字符串两边的空白字符
        rstrip  删除字符串右边的空白字符    lstrip左边的
'''
a = '   hello    '
b = a.strip()
print(b)
print(a.lstrip())
print(a.rstrip())


print('*'*20)
'''
        obj.center(len) 使字符串居中 并用空格填充至指定长度
        如果指定长度大于原本字符串长度 则原样输出
'''
a = 'abc'
b = a.center(20)
print(b)
print(a.center(2)) #也可以完整显示


print('*'*20)
'''
        obj.rjust(len) 右对齐 使用空格填充至指定长度    如果指定长度大于原本字符串长度 则原样输出
        obj.just(len) 左对齐 使用空格填充至指定长度     如果指定长度大于原本字符串长度 则原样输出
'''
c = a.ljust(20)
print(c)
c= a.rjust(20)
print(c)