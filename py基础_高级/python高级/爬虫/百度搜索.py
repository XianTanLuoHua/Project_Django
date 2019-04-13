"""
@author: XianTanLuoHua
@contact: 849317537@qq.com
@software: PyCharm
@file: 百度搜索.py
@time: 19-3-24 下午1:18
"""
from urllib import request
def main():
    url = 'https://www.baidu.com/s?wd=%E5%95%8A'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    urls = request.Request(url=url,headers=headers)
    response = request.urlopen(urls).read()
    html = response.decode('utf-8')
    with open('./test.03_html_css','w')as f:
        f.write(html)





if __name__ == "__main__":
    main()
