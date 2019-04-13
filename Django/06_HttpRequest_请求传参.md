# 请求

## 1.HttpRequest

> 服务器接收到http请求后会根据报文创建HttpRequest
> 视图的第一个参数就是HttpRequest对象
> 由Django创建之后调用视图是传递给视图
> 视图接收到的第一个参数就是HttpRequest

### 1.1属性参数

> path:请求的完整路径,不包括域名和端口
> method:请求的方式,常用的get和post
> encoding:表示浏览器请求的编码方式
> FILES:类似字典的对象包含了所有上唇的文件
> COOKIES:字典包含了所有的cookie
> seession:类似字典的对象,表示当前的会话

##### QueryDict对象

> GET:类似字典的对象包含了GET请求的所有参数
> POST:类似字典的对象包含了POST请求的所有的参数

	get():根据键获取值,只能获取一个
	getlist():将键的值以列表的形式返回,可以获取多个

### 1.2HttpRequest方法

	is_ajax():如果是通过ajax发起的则为true



## 2.http向服务器传参的方式



> 请求体（body）中发送的数据，比如表单数据、json、xml；
> 通过查询字符串
> 通过url传参
> Django中的QueryDict对象
> xml

### 2.1通过url路径传参

**2.1.1通过view视图函数中的request参数获取参数**

```
print(request.path)打印客户端发来的请求
```

**2.1.2按顺序传入**


	1.在urls中添加url(r'index_01/(\w+)/(\d+)/',users.views.index),将用户的访问url地址re匹配然后分组
	2.访问http://127.0.0.1:8000/index_01/aaa/1234/ 这个地址可以匹配上面的
	3.在views中响应的index函数中print(a,b) 打印aaa,1234 将按照**顺序**进行挨个传入

**2.1.3按关键字传入**

	1.在urls中按照正则规则给每个组命名url(r'index_02/(?P<year>[a-z]+)/(?P<day>\d+)/$',users.views.index_02)
	2.http://127.0.0.1:8000/index_02/aaa/1234/
	3.在views中响应的函数中 print(year,day) 打印aaa,1234将按照关键字参数方式传入


### 2.通过查询字符串传参(未完成)