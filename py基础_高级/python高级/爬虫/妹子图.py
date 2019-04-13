"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 妹子图.py
@time: 19-3-24 下午3:43
"""
import time
from urllib import request,parse
import re

def main():
    # for i in range(213):
    #     url = 'https://www.mzitu.com/page/{0}/'.format(i)
    #

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    url = 'https://www.mzitu.com/page/1/'

    url_data = request.urlopen(url)
    data = url_data.read().decode()
    p1 = re.compile(r'https://www.mzitu.com/\d+')
    p2 = re.compile(r'<span>\d+</span>')
    p3 = re.compile(r'\d+')
    p4 = re.compile(r'https://i.meizitu.net/\d+/\d+/\d+\S+')

    #匹配出来首页的每个妹子的地址后set去重
    p = set(p1.findall(data))

    over = set()
    for i in p:

        #进行判断是否已经采集 https://www.mzitu.com/174632
        if i not in over:
            print(i)
            #得到每个妹子的最大页码
            data = request.urlopen('{0}'.format(i)).read().decode()
            # print(data)
            a = p2.findall(data)
            print(a)
            # a = int(p3.findall(a[-1])[1]) #得到最大页码数量
            a = p3.findall(a[-1])
            a = int(a[0])


            for c in range(1,a+1):
                url_data = '{0}/{1}'.format(i,c)
                data_url = request.urlopen(url=url_data).read().decode()
                with open('./test{0}.03_html_css'.format(c),'w')as f:
                    f.write(data_url)



                #循环访问每页的网址
                # url_ = '{0}/{1}'.format(i,c)
                # url_one_data = request.urlopen(url).read().decode()
                # img_ong_map= p4.findall(url_one_data)[0] #得到图片的地址
                #
                # img_message = request.urlopen(img_ong_map)




                #匹配图片的每个网址并且进行保存











            for img in range():
                pass









            # over.add(i)
        else:
            pass









if __name__ == "__main__":
    main()
