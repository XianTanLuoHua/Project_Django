from urllib import request,parse
import json
def main(ipt):
    url ='https://fanyi.baidu.com/sug'
    data= {'kw':ipt}
    data = parse.urlencode(data).encode()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Content-Length':len(data)}
    rsp = request.Request(url=url,data=data,headers=headers) #组装请求
    rsp = request.urlopen(rsp)
    json_data = rsp.read().decode()
    json_data = json.loads(json_data)
    for i in json_data['data']:
        print(i['v'])
if __name__ == "__main__":
    while True:
        print('*'*100)
        ipt = input('--请输入想要翻译的文本--:')
        main(ipt)
