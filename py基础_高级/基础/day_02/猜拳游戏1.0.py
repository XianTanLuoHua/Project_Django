
# a = int(input('请输入您的成绩'))
# if a >= 60:
#
#     if a == 100:
#         print('恭喜您满分')
#     elif a > 100:
#         print('请输入正确的成绩')
#     else:
#         print('恭喜您及格了')
# else:
#     print('您的成绩太差了')

# a = int(input('请输入您的成绩'))
# if a >= 0 and a<=100:
#     if a >=60:
#         print('恭喜您及格了')
#     else:
#         print('您的成绩太差了')
# else:
#     print('请输入正确的数字')


class value__error(Exception):
    pass
import random as num
def next_():
    ipt = input('请问您还想玩吗? 按任意键继续 Y/N')
    if ipt == 'N' or ipt == 'n':
        print('欢迎下次来玩')
        raise value__error(len(0), 3)
while True:
    a = num.randint(1, 3)
    try:
        c = int(input('您想出\n1石头?\n2剪刀?\n3布?\n请输入序号:'))
        if c == 0 or c > 3 :
            raise value__error(len(0), 3)
        else:
            if c == a:
                print('您平局了game over')
                next_()
            elif (c == 1 and a == 2)or(c == 2 and a ==3)or(c == 3 and a == 1):
                print('您赢了game over')
                next_()
            else:
                print('您输了game over')
                next_()
    except:
        break








# d = 0
# for i in range(int(input('请输入想求的和'))+1):
#     d += i
# print(d)






