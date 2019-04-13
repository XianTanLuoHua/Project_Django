class Father():
    def show(self):
        print('我是老中医')

class Son(Father):
    def show(self):
        super().show()
        print('我也会西医')


if __name__ == '__main__':
    s = Son()
    s.show()