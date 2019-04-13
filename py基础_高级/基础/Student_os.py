import sys,os,time,random
sys.path.append(os.getcwd())


class student_mode():


    def __init__(self, stu_id, stu_name, stu_age):  # 创建一个学生模板  来接收传进来的信息
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age

    def __str__(self):
        return self.stu_id + '_' + self.stu_name + '_' + self.stu_age + '\n'



class student_sys():


    def __init__(self):
        self.__students = {}
        '''初始化用来存储信息的字典,Key为学生id,Vaule为student_model实例化后的对象'''


    '''打印菜单'''
    def __show_menu(self):
        print("*" * 30)
        print("欢迎使用【学生管理系统】 V1.0")
        print("1.添加学生")
        print("2.删除学生")
        print("3.修改学生")
        print("4.查询学生")
        print("5.显示全部")
        print("0.保存退出")
        print("*" * 30)


    '''定义一个输入学生信息的接口'''
    def __get_stu_info(self):
        stu_id = input('Please input Id:')
        stu_name = input('Please input Name:')
        stu_age = input('Please input Age:')
        return stu_id,stu_name,stu_age
    '''定义一个查询学生信息的接口'''
    def __find_one_info(self,stu):
        print('{0:<10}{1:<10}{2:<10}'.format(stu.stu_id,stu.stu_name,stu.stu_age))


    '''添加学生'''
    def __add_stu(self):
        stu_id,stu_name,stu_age = self.__get_stu_info()    #利用接口来获取用户输入,
        stu = student_mode(stu_id,stu_name,stu_age)        #将用户的输入拆包后当做参数传入类实例化后的对象
        '''以学生id为key 将 按照学生model实例化后的对象 为vaule'''
        self.__students[stu_id] = stu
        print('Add Over')


    '''删除学生'''
    def __del_info(self):
        ipt = input('Please input you need del Id:')
        if ipt in self.__students:                          #判断用户输入的信息是否在当前的字典内
            del self.__students[ipt]
            print('Id为{0}的学生删除成功'.format(ipt))
        else:
            print('Don\'t find your need del id')


    '''修改学生'''
    def __change_info(self):
        ipt = input('Please input you need del Id:')
        if ipt in self.__students:
            del self.__students[ipt]                         #直接把老的数据删掉
            stu_id,stu_name,stu_age = self.__get_stu_info()  #获取用户想修改的新的数值
            stu = student_mode(stu_id,stu_name,stu_age)      #使用用户输入的数值创建新的对象
            self.__students[stu_id]=stu                      #把对象存入字典中   Key为用户输入的id
        else:
            print('Don\'t find your need change id')


    '''查询学生'''
    def __find_info(self):
        ipt = input('Please input need student id:')
        if ipt in self.__students:
            print('{0:<10}{1:<10}{2:<10}'.format('StuId','Name','Age'))
            stu = self.__students[ipt]                       #把Kye对应的Value单独抽出来传进下方的函数
            self.__find_one_info(stu)
        else:
            print('Don\'t find your need id')


    '''查询全部'''
    def __find_all_info(self):
        print('{0:<10}{1:<10}{2:<10}'.format('StuId','Name','Age')) #格式化
        for stu in self.__students.values():                    #把字典中的Value 逐一抽取出来
            self.__find_one_info(stu)                           #调用查询接口  传入Value
        print('Find all over')


    '''写入文件'''
    def __stu_file(self):
        try:
            f = open('{0}\\stu_file.txt'.format(os.getcwd()),'w')
        except:
            print('read data except')
        else:
            for stu in self.__students.values():                    #把字典中的Value逐一抽取出来
                f.write(str(stu))                                   #调用的每个Value中对象的魔术方法
        finally:
            f.close()
            print('file over')


    '''读取文件'''
    def __stu_read_file(self):
        try:
            f_r = open('{0}\\stu_file.txt'.format(os.getcwd()),'r')
        except:
            print('read file except')
        else:
            f = f_r.readlines()
            for i in f:

                c1 = i.strip()                                        #数据清洗 除掉每行末尾的\n \t
                c2 = c1.split('_')                                    #以'_'进行分割 并返回一个字符串序列

                stu = student_mode(c2[0],c2[1],c2[2])                 #创建类的实例对象
                self.__students[c2[0]] = stu                          #把类实例对象的id作为Key,对象作为Value 添加到字典
        finally:
            print('\nload over')


    '''皮一下'''
    def __read_sleep(self):
        i = 0

        for i in range(101):
            print('\rlonging......{0}%'.format(i),end='')
            time.sleep(float(0.005))


    '''主控'''
    def __While_func(self):
        while True:
            '''循环打印菜单'''
            self.__show_menu()
            ipt = input('请按序号选择功能')

            '''判断用户输入'''
            if ipt == '1':
                self.__add_stu()

            elif ipt == '2':
                self.__del_info()

            elif ipt == '3':
                self.__change_info()

            elif ipt == '4':
                self.__find_info()

            elif ipt == '5':
                self.__find_all_info()

            elif ipt == '0':
                self.__stu_file()
                for i in range(10):
                    print('\rSaveing......',end='')
                    time.sleep(0.08)
                break

            else:
                print('输入的啥玩意重新写!')


    '''启动方法'''
    def start(self):
        self.__read_sleep()
        self.__stu_read_file()   #读取文件 把文件加载到内存
        self.__While_func()

st = student_sys()
st.start()