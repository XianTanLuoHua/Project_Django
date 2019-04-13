i = 0


def hano(a):
    hano_1(a, 'A', 'B', 'C')
    print('一共转移了{0}次'.format(i))


def hano_1(x, a, b, c):
    if x == 1:
        print('从', a, '柱子', '-->', c, '柱子')
    else:
        hano_1(x - 1, a, c, b)
        print('从', a, '柱子', '-->', c, '柱子')
        hano_1(x - 1, b, a, c)
    global i
    i += 1


hano(int(input('请输入汉诺塔的层数:')))
