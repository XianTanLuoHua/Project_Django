class cat():
    def __init__(self,color):
        self.color = color
        print('我是一个{0}猫'.format(self.color))

tom = cat('黄')
print(dir(tom))
print(tom.__dict__)
