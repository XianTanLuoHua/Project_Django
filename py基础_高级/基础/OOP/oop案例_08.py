class father():
    def show(self):
        print('祖传老中医')

class son(father):
    def show(self):
        print('留学回来 中西医结合')




if __name__ == '__main__':
    s = son()
    s.show()  #打印输出 留学回来 中西医结合
