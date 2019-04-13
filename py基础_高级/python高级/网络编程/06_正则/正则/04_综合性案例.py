#  ^ 以什么开始 python语言的match是自动添加的,其他语言不是这样,所以必须添加
# $以什么结尾
a = '''你是干什么的啊!
为什么这样啊'''

import re
names = ["age", "_age", "1age", "age1", "a_age!", "age_1_", "age!", "a#12#3", "------"]
p1 = re.compile('[a-z]+_*[a-z1-9_]*$',re.I)
for i in names:
    c = p1.findall(i)
    if c:
        print('匹配了',i)

    else:
        print('没有匹配',i)

# "^xxx$"  $ 这个就是匹配到尾

# 匹配变量名是否有效
# 匹配规则: 字母_开头, 匹配的数据: names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]
