# 响应

> 视图在接收请求并处理后，必须返回HttpResponse对象或子对象。
> HttpRequest对象由Django创建，HttpResponse对象由开发人员创建。
## 1. HttpResponse

### 属性

> content:表示返回的内容
> charset:表示返回的编码格式
> status_code:表示响应的状态码 100~599
> content_type:表示响应的MIME类型

### 方法:

> init:使用页面内容实例化HttpResponse对象
> write(content):以文件的形式写入
> flash():以文件的形式输出缓冲区
> set_cookie(key=cookie名, value=cookie值, max_age=cookie有效期)设置一个Cookie
> delete_Cookie(key):删除Cookie



**可以从 `django.http`里面导入`HttpResponse`**
**我们可以给这个对象设置一些参数**:

#### 设置一个json对象返回给客户端


```
使用方式: 
	def index(request):
		a='{"name": "python"}'
		return HttpResponse(s,content_type='application.json,status=400')


HttpResponse(
    content=响应体, 
    content_type=响应体数据类型, 
    status=状态码 100~599
)
```

#### **特别的使用方式:**

> 我们如果需要在***响应头***添加自定义的键值对内容,
> 可以把HttpResponse对象当做字典进行响应头键值对的设置：

***!!!对HttpResponse实例化***

```
def index_03(request):    
    response = HttpResponse('itcast python') #实例化之后顺便自定义了content
    response.status_code = 200    			 #自定义了状态码
    response['Itcast'] = 'Python'            #自定义了一个响应头
    return response
```



## 2. HttpResponse子类

> Django提供了一系列HttpResponse的子类，可以快速设置状态码
> 这个状态码可以从 `Django.http` 里面导入,例如:
> `from django.http import HttpResponseNotFound`

```HttpResponseRedirect 301
HttpResponsePermanentRedirect 302
HttpResponseNotModified 304
HttpResponseBadRequest 400
HttpResponseNotFound 404
HttpResponseForbidden 403
HttpResponseNotAllowed 405
HttpResponseGone 410
HttpResponseServerError 500
```

## 404

**通过在template文件夹下创建'404.html'的文件客户端在访问一个不存在的路径时,会自动给客户返回404文件**

> <h2>{{ request_path }}</h2>    可以获取到客户访问的路径进行打印




## 3. JsonResponse

> 如果我们要返回json字符串, 那么我们可以使用 JsonResponse 来帮助我们快速的构建json字符串,进行返回.
> JsonResponse 能够帮助我们自动把字典转成json字符串类型, 并且还不用自己设置响应头中contentType字段
> 所以总结一下, JsonResponse能够帮助我们做到如下两点:
> ***!!!自动帮助我们将数据转换为json字符串,设置响应头Content-Type为 application/json***

#### 使用:

```python
# 导入JsonResponse
from django.http import JsonResponse

def demo_view(request):
    # 直接通过JsonResponse类传入一个字典快速创建Json对象返回给浏览器
    #!注意,传入的对象需要是字典格式
    return JsonResponse({"name":"小明","age":18})
```
**如果使用JsonResponse类发送一个非字典格式的数据,需要设置safe=Flase**

	from django.http import JsonResponse
	def demo_view(request):
		a = [{"name":"小明"},{"age":18}]
		return JsonResponse(a,safe=Flase)



## 4.重定向

### 4.1redirect

> redirect内部使用的HttpResponse的对象

```
def index_06(request): #对客户端发来的请求进行重定向
    return redirect('/index_06_02/')
def index_06_02(request): #客户端转到的地址
    return HttpResponse('已经重定向访问到index_06_02了')
```
> 此时客户端访问index_06/服务器会重定向到index_06_02的地址

### 4.2HttpResponseRedirect
	def index_06(request): #对客户端发来的请求进行重定向
	    return HttpResponseRedirect('/index_06_02/')
	def index_06_02(request): #客户端转到的地址
	    return HttpResponse('已经重定向访问到index_06_02了')







