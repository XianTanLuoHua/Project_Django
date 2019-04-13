class person():
    name = '小明'


    @classmethod
    def show(cls): #类方法在定义时传入的参数并不是self 传入的是当前的对象
        print('我是用cls.name来访问类属性的',cls.name)
        print('我是__class__.name来访问类属性的',__class__.name)
        print('我是用person.name',person.name)





if __name__ == '__main__':
    person.show()


    print('*'*20)

    p1 = person()
    p1.show()
