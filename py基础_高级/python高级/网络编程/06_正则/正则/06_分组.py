# | 相当于python中的or
# 	案例:匹配出163或者126的邮箱


# ()还可以单独取出匹配的某一部分数据
# 	案例:取出邮箱的类型(只要163,126),后期可以编计用户那个邮箱用的多
import re
a1 = '849317537@qq.com'
a2 = '849317537@163.com'
a3 = '849317537@163.com849317537@qq.com849317537@163.com849317537@qq.com'

p1 = re.compile('(qq|163)')
print(p1.findall(a2))
print(p1.findall(a1))
print(p1.findall(a3))





# \num用来取第几组用()包裹的数据  \1取第一个内部的括号位置的值
# 格式(xxx)\1 :\1表示获取(xxx)的值
# 案例<html>hh</html>  # 这个一定是有字母,开始跟结束的字母必须一样

str = "<html>hh</html>"


str = "<html><body>hh</body></html>"





# 案例<html><body>hh</body></html>
str_data = "<html><body>hh</body></html>"

# 使用别名给分组取别名,了解一下
# 格式:(?P<别名>xxx)(?P=别名)
# 案例<html><body>hh</body></html>
# 提示问题没错
