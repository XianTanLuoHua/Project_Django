"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 妹子图.py
@time: 19-3-24 下午3:43
"""
from urllib import request,parse
import re

def main():
    # for i in range(213):
    #     url = 'https://www.mzitu.com/page/{0}/'.format(i)
    #


    url = 'https://www.mzitu.com/page/1/'

    url_data = request.urlopen(url)
    data = url_data.read().decode()
    p1 = re.compile(r'https://www.mzitu.com/\d+')
    p2 = re.compile(r'<span>\d</span>')
    p3 = re.compile(r'\d+')
    p4 = re.compile(r'https://i.meizitu.net/\d+/\d+/\d+\S')

    #匹配出来首页的每个妹子的地址后set去重
    p = set(p1.findall(data))

    over = set()
    for i in p:

        #进行判断是否已经采集 https://www.mzitu.com/174632
        if i not in over:

            #打开一次妹子主页得到每个妹子的最大页码
            data = request.urlopen('{0}'.format(i)).read().decode()
            a = p2.findall(data)
            max = int(p3.findall(a[1])[0]) #得到最大页码数量
            for i in range(1,max+1):






            for i in range(1,a+1):
                #循环访问每页的网址
                url_ = '{0}/{1}'.format(i,i)
                url_one_data = request.urlopen(url).read().decode()
                img_ong_map= p4.findall(url_one_data)[0]
                img_get = ''




                #匹配图片的每个网址并且进行保存











            for img in range():
                pass









            over.add(i)
        else:
            pass









if __name__ == "__main__":
    main()
