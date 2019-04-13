"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: py调用mysql常用操作.py
@time: 19-4-1 上午11:14
"""
import pymysql

def main():
    try:
        #创建与数据库连接的对象
        coon = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='2233',database='jing_dong',charset='utf8')

        #获得游标对象来完成增删改查
        cur = coon.cursor()

        #设置要执行的sql语句
        sql = 'select * from goods'

        #使游标对象执行sql语句,并且得到该语句影响的行数
        cur.execute(sql)
        # count_line = cur.execute(sql)
        # print('sql语句执行后一共影响了{0}行'.format(count_line))

        #接取游标对象执行后的结果
        data = cur.fetchall()
        print('执行后的结果用   游标对象.fetchall()来获取')
        for i in data:
            print(i)


        #对数据进行修改

        #对数据库的name字段进行插入
        # sql = 'insert into goods(name) values("哈哈"),("啊");'

        #对数据库进行条件删除
        sql = "delete from goods where name = '哈哈'"

        #对数据库进行条件修改
        sql = "update goods set name = '你好a' where id =32"

        count_line = cur.execute(sql)

        #对内存中的操作 用连接对象进行提交
        coon.commit()

        #关闭游标
        cur.close()

        #关闭连接
        coon.close()
    except Exception as s:

        #如果捕捉到异常 则进行回滚
        coon.rollback()
        print(s)

if __name__ == "__main__":
    main()
