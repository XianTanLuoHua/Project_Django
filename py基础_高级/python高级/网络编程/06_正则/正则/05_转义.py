# \进行转义
# 在正则特殊的符号, 想以字符串的形式使用使用转义
# 匹配出163的邮箱地址，且 @ 符号之前有4到20位字符, 以.com结尾

user = '我的邮箱是849317537@qq点com我的邮箱是849317537@qq.com'

import re
p1 = re.compile('\d+.\w+\.com$')
print(p1.findall(user))