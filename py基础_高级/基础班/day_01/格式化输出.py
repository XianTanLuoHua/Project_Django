'''
        %s str类型
        %d 整数类型
        %f 浮点类型
        %.2f 精确到2位小数
'''
print('%06d' % 85)  # 代表6位数 如果不够用0在左侧填充
def people_1(name, age, height):
    print('我叫%s,年龄%-5d,身高%.2fcm' % (name, age, height)) # %5d代表往左边填充把元素放到第五位,-负号反之
people_1('小明', 20, 198.2)
print('*' * 20)


'''
        f'string' 对于浮点数无法精确位数   这种方法需要关键字有相应的value
'''
def people_2(name, age, height):
    print(f'我是{name},今年{age},身高{height}cm')
people_2('小明', 20, 198.256)
print('*' * 20)


'''
        format   常用  按照填充的索引 or 填充的key对应key指向的value
'''
def people_3(*args):  # 收集参数
    print('我叫{0},今年{1}岁了,身高{2}cm'.format(*args))
people_3('小明', 22, 198.214)

'''
        format 填充操作   '{索引:填充符  ><^想哪里对齐  总共多少位}'.format(下标索引0的元素)
'''
print("{0}*{1}={2:0>2}".format(3, 2, 2 * 3))
print("{:*^30}".format('centered'))  # ^中间对齐
print("{: >30}".format('right'))  # > right 向右边靠齐
print('{0:*<30}'.format('left'))  # < left 左
