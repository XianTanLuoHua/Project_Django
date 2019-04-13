import os


''''
        文件操作
            路径解释
                . 一个点表示当前目录
                .. 表示当前目录的上一级目录
                / 目录分隔符
'''

'''
        重命名文件 os.rename(oldname,newname)
'''

'''
        删除文件  os.remove(filename)
'''

'''
        创建文件夹 os.mkdir()
            如果存在同名文件夹 则报错
'''


'''
        获取当前执行目录 os.getcwd()
'''

'''
        改变当前目录 os.chdir()
'''

'''
        列出当前目录中的文件列表 os.listdir() 
'''

'''
        删除文件夹 os.rmdir(dir)  如果目录下有文件则无法删除
'''


for i in os.listdir():
    r = open('./'+i,'rb')
    old_path =i.partition('.')
    f = open(r'C:\Users\84931\Desktop\test_copy\\'+old_path[0]+'copy'+old_path[1]+old_path[2],'wb')
    f.writelines(r)
