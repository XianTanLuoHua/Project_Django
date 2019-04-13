#

'''
        try:
            放需要捕捉异常的代码
        except:
            放异常之后的处理
        else:
            会在try句子中没有任何异常的时候执行
        finally:
            最后要执行的代码无论有没有异常
'''

# try:
#     num1 = int(input('请输入第一个数字'))
#     num2 = int(input('请输入第二个数字')) #输入0试试
#     if num2 == 0 :
#         raise ZeroDivisionError
# except ZeroDivisionError:
#     print('0不能被除')


# '''
#         如果想报两个错误可以让except(error1,error2)来表示
# '''
#
# try:
#     num1 = int(input('请输入第一个数字'))
#     num2 = int(input('请输入第二个数字'))
#     if num2 == 0 :
#         raise ZeroDivisionError
# except (ZeroDivisionError,ValueError)as e:  #这次输入a试试
#     print(e)
#     print('请输入正确数值')

# '''
#         异常捕捉是从上往下处理的 只会捕捉一个
# '''
# try:
#     a = input('请输入1或者a')
#     if a =='a':
#         raise NameError
#     elif a =='1':
#         raise ValueError
# except NameError: #如果捕捉到了NameError 就不会执行下面的异常剥啄了
#     print('名字错了')
# except Exception:
#     print('捉到了')


# '''
#         如果不想显示任何信息还是使用raise参数 不显示任何信息即可
# '''
# try:
#     num1 = int(input('请输入数字'))#输入a试试
# except(ValueError):
#     print('不带这个print就是啥也不输出了 只给报错信息')
#     raise



# '''
#         不想做什么处理   还是显示系统异常信息
#         把捕捉的异常通过 as 关键字存入变量，然后显示输出这个存进去的变量
# '''
# try:
#     num1 = int(input('请输入数字'))#输入abc 或者0试试
#     a = 1/num1
#
# except(ValueError,ZeroDivisionError) as c: #异常存进变量里面打印出来
#     print(c)




# '''
#         我们也不知道发生了什么异常 用except什么都不添加即可
# '''
# try:
#     num1 = int(input('哈哈哈输入数字吧'))
# except:
#     print('发生了一亗错误，但不知道是什么！')



# '''
#         我们也不知道发生了什么异常 用except什么都不添加即可  显然这样不太信
#         那就用标准异常的超类Exception来帮我们获得所有异常 并用as保存到变量中
# '''
# try:
#     num1 = int(input('请输入数字啊'))
# except Exception as e:
#     print(e)
#


# '''
#         else  如果try中没有异常就会执行
#         finally 最后无论有没有异常都会执行的语句
# '''
# try:
#     num  = int(input('请输入数字  你也可以看看输出字母会输出什么'))
# except:
#     print('您输入错了')
# else:
#     print('只有没有异常的时候我才会被执行')
# finally:
#     print('无论有没有异常都会被执行')


'''
        异常的传递
'''

def func_a():
    print('a开始了')
    func_b()
    print('a结束')

def func_b():
    print('b开始了')
    try:
        func_c()
    except Exception:
        print('调用的函数发生了异常')
    print('b结束')

def func_c():
    print('c开始了')
    print('haha',n)
    print('c结束')

func_a()







