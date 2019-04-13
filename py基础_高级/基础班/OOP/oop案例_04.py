''
'''
        
'''
import time

class potato():
    def __init__(self): #初始化烤地瓜状态
        #创建两个实例属性并初始化
        self.time = 0
        self.starts ='生的'


    def __str__(self):
        resutlt = '地瓜被烤了{0}分钟,现在烤了{1}分熟'.format(self.time,self.starts)
        return resutlt
    def __del__(self):
        print('地瓜被扔了')


    def cook(self,cool_time):
        # 实现判断逻辑 根据时间改变状态
        self.time +=cool_time
        if self.time<3:
            self.starts = '生的'
        elif self.time <=6:
            self.starts = '半生不熟'
        elif self.time <=8:
            self.starts = '烤熟了'

        else:
            print('烤糊了')



if __name__ == '__main__':
    obj_1 = potato()
    print(obj_1)
    obj_1.cook(4)
    print(obj_1)
    obj_1.cook(3)
    print(obj_1)
    '''
            如果不加这条件 则程序运行之后 会自动释放资源 自动执行这个函数
    '''
    time.sleep(100)