class A():
    def __init__(self,a,b):
        super().__init__(b)
        self.a = a
class B():
    def __init__(self,b):
        self.b=b
class C(A,B):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
if __name__ == '__main__':
    c = C('1','2','3')

    print(c.c)
    print(c.b)
    print(c.a)

'''
        执行步骤 1 初始化C的时候传进来3个数   自动对应了 abc    c被赋值给了self.c    
        其中调用了super()__init__(a,b)函数 根据mro的顺序找到了C的上一层的父类 是A   吧ab传入A    
        然后进入A执行super()__init__(b)方法  把b按照mro的顺序传入了B中      a自动执行赋值操作self.a = a
        因A调用了super()__init__(b)  所以继续往上找按照mro顺序找到了B 把b传入B    b赋值给了self.b = b
        
        都赋值完毕 数据一步一步返回 self.a = a   self.b = b   self.c = c    self是被实例化后的c
'''