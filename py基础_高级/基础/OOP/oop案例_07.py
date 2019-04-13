class stu():
    def __init__(self,name):
        self.name = name
        self.__age = 20

    def set_age(self,set_age):
        self.__age = set_age

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    stu1 = stu('小明')
    print(stu1.name)
    print(stu1.get_age())
