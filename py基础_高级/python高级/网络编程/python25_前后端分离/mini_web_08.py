# 根据不同的地址返回不同的响应数据
import json

from pymysql import connect

# 装饰器
# 装饰前的函数是由func指向的
# 装饰后的函数调用的其实是call_fun
# 道德上不允许修改原先函数的返回值及参数

# 装饰传参自动完成注册的字典

url_dict = dict()


# 对应的请求的地址
def set_url(url):
    def set_fun(func):
        print("被装饰的函数:", func)
        print("被装饰的对应url:", url)

        # 添加到字典中
        # url_dict[url] = func

        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        # 这个放的是装饰后的函数
        url_dict[url] = call_fun

        return call_fun

    return set_fun


# 入口函数
# 一个页面一个函数
def application(file_path):
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"

    # 响应头
    response_head = "content-type:text/html;charset=utf-8;\r\n"

    # 如果if跟else超过三个以上可以使用字典
    # # 创建一个字典
    # url_path = dict()
    # # 添加函数引用与函数的地址
    # url_path['/index.html'] = index
    # url_path['/center.html'] = center
    # url_path['/login.html'] = login
    print("自动生成的字典:", url_dict)
    try:
        # 得到函数引用
        # func = url_dict[file_path]
        # response_body = func()

        response_body = url_dict[file_path]()
    except Exception as e:
        print("异常:", e)
        # 找不到网页
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "not page is show!"

    # if file_path == "/index.html":
    # 	response_body = index()
    #
    # elif file_path == "/center.html":
    # 	response_body = center()
    #
    # else:
    # 	# 找不到网页
    # 	response_line = "HTTP/1.1 404 NOT FOUND\r\n"
    #
    # 	response_body = "not page is show!"

    return response_line, response_head, response_body


################################上面就是框架了###################################

@set_url("/center.html")
def center():
    # 1.返回 前端的界面
    with open("./templates/center.html") as f:
        content = f.read()
    return content


@set_url("/center_data.html")
def center_data():
    print("请求数据:")
    # 1.去数据库得到数据库的数据
    # 1. 从数据库得到数据
    # 1.1连接数据库
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 1.2 执行查询的sql语句
    cs1.execute(
        """SELECT info.code,info.short,info.chg,info.turnover,info.price,info.highs,focus.note_info from info INNER  JOIN focus on info.id = focus.info_id;""")
    # 得到数据库的数据
    data = cs1.fetchall()

    # 1.3 关闭
    cs1.close()
    conn.close()

    # for temp in data:
    # 	print(temp)
    # 2.拼接我们的json格式的数据
    # 整体是一个列表,列表中有多个字典

    data_list = list()

    for temp in data:
        # 定义一个字典
        # Decimal('13.57')需要 转成字符串
        data_dict = dict()
        data_dict['code'] = temp[0]
        data_dict['short'] = temp[1]
        data_dict['chg'] = temp[2]
        data_dict['turnover'] = temp[3]
        data_dict['price'] = str(temp[4])
        data_dict['highs'] = str(temp[5])
        data_dict['note_info'] = temp[6]

        # 添加到列表中
        data_list.append(data_dict)

    # print(data_list)

    # json解析的工具
    data_json = json.dumps(data_list)

    print("json:", data_json)

    return data_json
