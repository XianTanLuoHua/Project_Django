class ClassRoom():
    kongtiao = 'geli'

    def __init__(self):
        self.jiaoshi = 207
        self.mingzi = 'python25'

    def show(self):
        print('下面调用函数在类的内部进行访问类属性')
        print(__class__.kongtiao)
        print(ClassRoom.kongtiao)




if __name__ == '__main__':
    js207 = ClassRoom()# 使用实例对象来调用类属性
    print(js207.kongtiao)

    print(ClassRoom.kongtiao)  #使用类本身来调用类属性


    js208 = ClassRoom()
    print(js208.kongtiao)




    ClassRoom.kongtiao = '美的'   #对类中的属性进行修改
    print(js207.kongtiao)       #会影响到实例对象


    js208.show()

