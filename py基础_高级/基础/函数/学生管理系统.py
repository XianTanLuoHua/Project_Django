import time
import os, sys
import threading
from pynput.keyboard import Controller, Key, Listener


def on_release(key):
    if key == Key.esc:
        return False


def start_listen():
    with Listener(on_release=on_release) as listener:
        listener.join()


all_stu_info = []  # 创建一个全局变量来接收学生列表


def print_menu():  # 菜单
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有")
    print(" 6:保存数据")
    print("   按esc退出")
    print("---------------------------")


def change_stu_info():
    stu_info = {}
    stu_info['id'] = input('请输入学生学号:')
    stu_info['name'] = input('请输入学生姓名:')
    stu_info['sex'] = input('请输入学生性别:')
    stu_info['age'] = input('请输入学生年龄:')
    stu_info['time'] = time.ctime()
    all_stu_info.append(stu_info)


def add_stu():  # 创建一个添加函数
    change_stu_info()
    print('添加完毕了哦')


def del_stu():  # 删除属性
    del_stu_info = input('请输入要删除的学生的学号:')
    for i in all_stu_info:
        if del_stu_info == i['id']:
            all_stu_info.remove(i)
            print('已经删除了id为{0}学生的数据哦'.format(del_stu_info))
            break
        else:
            print('没找到要删除的哦')


def change_stu():  # 修改学生
    change_info = input('请输入要修改的学生的学号:')
    for i in all_stu_info:
        if change_info == i['id']:
            i['id'] = input('请输入修改后的id:')
            i['name'] = input('请输入修改后的名字:')
            i['sex'] = input('请输入修改后的性别:')
            i['age'] = input('请输入修改后的年龄:')
            i['time'] = time.ctime()
            print('修改完毕了哦')
            break
    else:
        print('没找到要修改的哦')


def info_one_stu(stu):  # 定义一个用来打印学生信息的函数 传进来一个字典
    print('{0:<10}{1:<10}{2:<10}{3:<10}{4:<10}'.format(stu['id'], stu['name'], stu['sex'], stu['age'], time.ctime()))


def info_stu():  # 查询单个学生
    stu_info = input('请输入需要查询的学生的id:')
    print('{0:<10}{1:<10}{2:<10}{3:<10}{4:<10}'.format('id', 'name', 'sex', 'age', 'change_time'))
    for i in all_stu_info:
        if stu_info == i['id']:
            info_one_stu(i)
            print('查询完毕了哦')
            break
    else:
        print('没找到要找的哦')


def all_stu():  # 打印所有的的学生
    print('{0:<10}{1:<10}{2:<10}{3:<10}{4:<10}'.format('id', 'name', 'sex', 'age', 'change_time'))
    for i in all_stu_info:
        info_one_stu(i)
    print('查询完毕了哦')


def main():  # 主控
    while True:
        print_menu()
        user_iup = input('请输入序号选择功能(按esc键退出):')

        if user_iup == '1':
            add_stu()
        if user_iup == '2':
            del_stu()
        if user_iup == '3':
            change_stu()
        if user_iup == '4':
            info_stu()
        if user_iup == '5':
            all_stu()
        if user_iup == '6':
            pass


if __name__ == '__main__':
    mainthr = threading.Thread(target=main, args=())
    mainthr.setName('func1')
    mainthr.setDaemon(True)
    mainthr.start()

    kb = Controller()
    kb.press(Key.space)
    start_listen()
