# -- 匹配的规则
# 字符	    功能
# *	    匹配前一个字符出现0次或者无限次，即可有可无
# +	    匹配前一个字符出现1次或者无限次，即至少有1次
# ?	    匹配前一个字符出现1次或者0次，即要么有，要么没有
# {m}	    匹配前一个字符出现m次  \d{3}
# {m,n}	匹配前一个字符出现从m到n次  \d{4,6}

import re
print('---------------------------------------------------------------1')
# 使用  类型{}
# 用来表示一个字符出现多少次
# 匹配速度与激情1,速度与激情12
a = '匹配速度与激情1,速度与激情12'
p1 = re.compile('速度与激情\d{2}')
print(p1.findall(a))


print('---------------------------------------------------------------2')
# 匹配手机号11位
p2 = re.compile('\d{11}')
a = '12345678901123'
print(p2.findall(a))





print('---------------------------------------------------------------3')
# 判断电话号码是否021 - 开头的后面8位电话号码
# 例: 021 - 12345678
# 判断电话号
p1 = re.compile('010\s?-?\s*\d+')
a = '0101234124124'
b = '010-   123141241'
print(p1.findall(a))
print(p1.findall(b))



print('---------------------------------------------------------------4')
# 使用?
# 用来表示有一个字符或者没有字符
# 用户输入的电话号码有时有'-'有时没有
# 例:02112345678 或者  021-12345678
p1 = re.compile('\d+\s*-?\s*\d+')
a = '02112345678 或者  021  -     12345678'
print(p1.findall(a))




print('---------------------------------------------------------------5')
# 有些地方是三位电话号码开头,有些是四位电话号码开头
a='0157 -   8123456'
b='021-        12345678'
p1 = re.compile('\d{3,4}\s*-+\s*\d+')
print(p1.findall(a))
print(p1.findall(b))




print('---------------------------------------------------------------6')
# *
# 表示0或者无限次
# 匹配一段文字或者没有输入文字

str = """今天天气不错
我们可以出去运动一下!
"""
print(re.compile('\w+\s\w+').findall(str))

# +
# 表示至少一次,不能为空
