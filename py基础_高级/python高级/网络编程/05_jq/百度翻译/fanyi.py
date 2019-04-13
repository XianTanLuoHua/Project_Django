"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 百度翻译.py
@time: 19-3-24 下午2:35
"""

from urllib import request,parse
import json


def main(ipt):
    '''
    利用data构造请求内容然后用urlopen打开
    返回一个json的结果
    结果就是girl的释义
    :return:None
    '''

    url ='https://fanyi.baidu.com/sug'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    #请求提存放模拟form的数据一定是dict格式, 字符需要需要进行parse解码成浏览器的文本,然后再进行编码成字节流
    data= {'kw':ipt}
    data = parse.urlencode(data).encode()


    #构造一个请求头,请求头至少包含传入的数据的长度len(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Content-Length':len(data)
    }

    #有了请求头 请求体 组装请求
    rsp = request.Request(url=url,data=data,headers=headers) #组装请求
    #打开请求
    rsp = request.urlopen(rsp)

    json_data = rsp.read().decode()
    # print(json_data) #打印发现是json格式  需要用json包解码

    #loads加载json包
    json_data = json.loads(json_data)


    return json_data['data']



def ipt(message):
    return main(message)



if __name__ == "__main__":
    #打开f12  尝试输入girl  发现每次敲一个字母都有请求 请求地址是https://fanyi.baidu.com/sug
    # 发现form Data是一个字典的键值对 值为girl
    # 检查响应体发现返回类型是josn类型  需要用到json包
    while True:
        ipt_01 = input('请输入想要翻译的英文')
        print(main(ipt_01))

