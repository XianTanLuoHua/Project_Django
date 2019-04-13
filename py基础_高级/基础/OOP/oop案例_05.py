#有一个狗类
    #有宠物狗属性
    #有体格叫的方法


class Dog():
    def __init__(self,name):
        self.name = name
    def bark(self):
        print('汪汪汪{0}'.format(self.name))


#有一个人类
    #有一个宠物的属性
    #人类想听狗叫
class person():
    def __init__(self,name,pet):
        self.name = name
        self.pet = pet


#定义一个听宠物叫的方法
    def listen_dog(self):
        self.pet.bark()


if __name__ == '__main__':

    tom = person('tom',Dog('golf'))

    tom.listen_dog()