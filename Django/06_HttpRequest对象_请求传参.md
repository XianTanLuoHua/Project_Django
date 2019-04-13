# 请求

## 1.HttpRequest

> 服务器接收到http请求后会根据报文创建HttpRequest对象
> 视图的第一个参数就是HttpRequest对象
> 由Django创建之后调用视图时传递给视图
> 视图接收到的第一个参数就是HttpRequest

### 1.1属性参数

> request.path:请求的完整路径,不包括域名和端口
> request.method:请求的方式,常用的get和post
> request.encoding:表示浏览器请求的编码方式,none表示浏览器使用的默认配置'utf-8'
> request.FILES:类似字典的对象包含了所有上传的文件
> request.COOKIES:字典包含了所有的cookie
> request.seession:类似字典的对象,表示当前的会话
> request.body:包含了请求体内的数据
> request.user:请求的用户对象

##### QueryDict对象:是一个类似字典的对象

> request.GET 指的不是发送ajax用的get方法, 而是指从url的查询字符串中获取参数
> request.POST 指的也不是ajax用的post方法,而是我们从请求体中获取的参数


 **GET 和 POST 这里指的都是获取参数的位置, 而不是我们以前说的get请求和post请求.**
 **QueryDict对象的方法:**

	通过客户发起请求的HttpRequest对象得到.
	get():根据键获取值,只能获取一个,如果有多个则获取最后一个
		客户访问http://127.0.0.1:8000/index_08/?a=1&b=2
		服务器得到 print(QueryDict.get('a'),request.GET.get('b')) 打印
	getlist():将键的值以列表的形式返回,可以获取多个
		客户访问http://127.0.0.1:8000/index_08/?a=1&b=2&a=3&b=4
		服务器的到print(QueryDict.getlist('a'),request.GET.getlist('b'))

### 1.2HttpRequest方法

	is_ajax():如果是通过ajax发起的请求,则为true



## 2.http向服务器传参的方式

> 请求体（body）中发送的数据，比如表单数据、json、xml；
> 通过查询字符串
> 通过url传参
> Django中的QueryDict对象
> xml



### 2.1通过url路径传参

**2.1.1通过view视图函数中的request参数获取参数**

```
print(request.path)打印客户端发来的参数
```

**2.1.2按顺序传入**


	1.在urls中添加url(r'index_01/(\w+)/(\d+)/',users.views.index),将用户的访问url地址re匹配然后分组
	2.访问http://127.0.0.1:8000/index_01/aaa/1234/ 这个地址可以匹配上面的
	3.在views中响应的index函数中print(a,b) 打印aaa,1234 将按照**顺序**进行挨个传入

**2.1.3按关键字传入**

	1.在urls中按照正则规则给每个组命名url(r'index_02/(?P<year>[a-z]+)/(?P<day>\d+)/$',users.views.index_02)
	2.http://127.0.0.1:8000/index_02/aaa/1234/
	3.在views中响应的函数中 print(year,day) 打印aaa,1234将按照关键字参数方式传入



### 2.2通过查询字符串传参

**重要：**
> *查询字符串不区分请求方式，即假使客户端进行POST方式的请求，依然可以通过request.GET获取请求中的查询字符串数据**

**注意:**
> 这里的 request.GET 指的不是发送ajax用的get方法, 而是指从url的查询字符串中获取参数
> 同理: request.POST 指的也不是ajax用的post方法,而是我们从请求体中获取的参数

**GET 和 POST 这里指的都是获取参数的位置, 而不是我们以前说的get请求和post请求.**

	通过客户发起请求的HttpRequest对象得到.
	get():根据查询字符串中键获取值,只能获取最后一个
		客户访问http://127.0.0.1:8000/index_08/?a=1&b=2
		服务器得到 print(request.GET.get('a'),request.GET.get('b')) 打印
	getlist():将查询字符串中键的值以列表的形式获取,可以获取多个
		客户访问http://127.0.0.1:8000/index_08/?a=1&b=2&a=3&b=4
		服务器的到print(request.GET.getlist('a'),request.GET.getlist('b'))


### 2.3通过请求体传参

#### 2.3.1表单类型

> 请求体数据格式不固定，可以是表单类型字符串，可以是JSON字符串，可以是XML字符串，应区别对待。
> 可以发送请求体数据的请求方式有 **POST**、**PUT**、**PATCH**、**DELETE**。

**Django默认开启了CSRF防护**，会对上述请求方式进行CSRF防护验证，在测试时可以关闭CSRF防护机制，方法为在settings.py文件中注释掉CSRF中间件,在settings.py中MIDDLEWARE这个列表中

	print(request.POST.get('a')) 得到请求体中指定的数据
	print(request.POST.getlist('a')) 将请求体中键的值以列表的形式获取,可以获取多个
#### 2.3.2非表单类型

> 非表单类型的请求体数据，Django无法自动解析
> 可以通过**request.body**属性获取最原始的请求体数据，自己按照请求体格式（JSON、XML等）进行解析。
> 其中: **request.body返回bytes类型。**

**例如:**
> 要获取请求体中的如下JSON数据
```
{"a": 1, "b": 2}
```
可以进行如下方法操作：

```
import json

def get_body_json(request):
    json_bytes = request.body
    json_str = json_bytes.decode()

    #python3.6及以上版本中, json.loads()方法可以接收str和bytes类型
    #但是python3.5以及以下版本中, json.loads()方法只能接收str, 所以我们的版本如果是
    #3.5 需要有上面的编码步骤.

    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')
```
### 2.4通过请求头传参

> 我们可以通过**request.META**属性获取请求头headers中的数据
> **request.META为字典类型**。

**这里需要注意一点是: 我们平常见到的请求头是这样的:**

```
POST /reqresp/req/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
Postman-Token: dd531a45-7518-1e8f-63a5-be03ed593471

a=1&b=2&a=3
```
**但是我们通过request.META获取的时候,需要使用如下所示的用法:**

	CONTENT_LENGTH – 请求主体的长度
	CONTENT_TYPE – 请求主体的MIME类型
	HTTP_ACCEPT – 响应的可接受内容类型
	HTTP_ACCEPT_ENCODING – 响应的可接受编码
	HTTP_ACCEPT_LANGUAGE – 响应的可接受语言
	HTTP_HOST – 客户端发送的HTTP主机头
	HTTP_REFERER – 引用页面(如果有)
	HTTP_USER_AGENT – 客户端的用户代理字符串
	QUERY_STRING – 得到查询字符串
	REMOTE_ADDR – 客户端的IP地址
	REMOTE_HOST – 客户端的主机名.
	REMOTE_USER – 由Web服务器验证的用户(如果有)
	REQUEST_METHOD – 请求的方式
	SERVER_NAME – 服务器的主机名
	SERVER_PORT – 服务器的端口

**具体使用如:**

	def get_headers(request):
	    print(request.META['CONTENT_TYPE'])
	    return HttpResponse('OK')
