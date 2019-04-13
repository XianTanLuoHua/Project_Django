import urllib.request
from urllib.parse import quote
from lxml import etree
import random
import requests
import re
import os
import gzip
uapools = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #   'accept-encoding':'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1544957840; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1544965267',
        'Pragma': 'no-cache',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36,'

}
def get_html(url):

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    try:
        html = gzip.decompress(html).decode("utf-8")
    except OSError:
        pass
    return html
def get_image(url,referer):
    #网站限制，不能直接访问某个网址，要从上一个网页跳转才可以访问。这里referer模拟从别的网页跳转
    headers['referer']=referer
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html
def saveImgToLocal(name,dict):
    path = "meizitu/" + name+ "/"

    for key in dict.keys():
        print(key)
        try:
            new_path=path+key+'/'
            if not os.path.isdir(new_path):
                os.makedirs(new_path)
            try:
                html = get_html(dict[key])
            except OSError:
                continue
            content = etree.HTML(html)
            len_path="//div[@class='pagenavi']/a/span/text()"
            length=content.xpath(len_path)[-2]

            url_path="//div[@class='main-image']/p/a/img/@src"
            url=content.xpath(url_path)[0][:-6]
            for i in range(1,int(length)+1):
                if i <10:
                    str_i='0'+str(i)
                else :
                    str_i=str(i)
                new_url=url+str_i+'.jpg'

                print(new_url)

                pic=get_image(new_url,dict[key])
                image_path=new_path+str_i+'.jpg'
                fp=open(image_path,'wb')
                fp.write(pic)
                fp.close()

        except requests.exceptions.ConnectionError:
            continue




def loadNextLink(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     #   'accept-encoding':'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=15fa02251e679e-05c01fdf7965e7-5848211c-144000-15fa02251e7800; bdshare_firstime=1510220189357; CNZZDATA1263415983=1653134122-1510216223-null%7C1510216223; CNZZDATA3866066=cnzz_eid%3D376479854-1494676185-%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1510220189; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1510220990',

        'Pragma': 'no-cache',
        'User-Agent': random.choice(uapools)}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    html=response.read()
    #这个网站有的返回的html是压缩的有的不是压缩的
    try:
        html=gzip.decompress(html).decode("utf-8")
    except OSError:
        pass

    content = etree.HTML(html)
    link_path="//ul[@id='pins']/li/span/a/@href"
    name_path="//ul[@id='pins']/li/span/a/text()"
    link=content.xpath(link_path)
    name=content.xpath(name_path)
    dict={}
    for i in range(len(name)):
        dict[name[i]]=link[i]
    return dict
if __name__ == '__main__':
    name=input("名字")

    url="https://www.mzitu.com/search/"+quote(name)+"/"
    dict=loadNextLink(url)
    saveImgToLocal(name,dict)
