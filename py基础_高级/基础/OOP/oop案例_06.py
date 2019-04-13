class house():
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        print('这个家具叫{0}面积{1}'.format(self.name,self.area))



class home():
    def __init__(self):
        self.maps = '北京三环'
        self.sum_area = 100
        self.keyong  = self.sum_area
        self.jiajuLST= []


    def add_area(self,item):
        if self.keyong >= item.area:
            self.jiajuLST.append(item)
            self.keyong  = self.keyong-item.area
            print(item)
        else:
            print('面积不够大')

    def __str__(self):
        info = '我家在{0}装完家具 面积还剩{1}'.format(self.maps,self.keyong)
        for item in self.jiajuLST:
            info= info+str(item) + '\n'
            return  info


if __name__ == '__main__':
    home = home()

    bed1 = house('单人床', 3)
    home.add_area(bed1)



    print(home)
