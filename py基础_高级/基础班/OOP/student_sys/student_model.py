'''
        创建一个学生的模板
'''


class student_mode():
    def __init__(self,stu_id,stu_name,stu_age):  #创建一个学生模板  来接收传进来的信息
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age

    def __str__(self):
        return self.stu_id+'_'+self.stu_name+'_'+self.stu_age+'\n'
