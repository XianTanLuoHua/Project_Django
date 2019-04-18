# sisson

## 1. 启用Session

### 简介:

> Session:在计算机中，尤其是在网络应用中，称为“会话控制”。Session 对象存储特定用户会话所需的属性及配置信息。这样，当用户在应用程序的 Web 页之间跳转时，存储在 Session 对象中的变量将不会丢失，而是在整个用户会话中一直存在下去。当用户请求来自应用程序的 Web 页时，如果该用户还没有会话，则 Web 服务器将自动创建一个 Session 对象。当会话过期或被放弃后，服务器将终止该会话。Session 对象最常见的一个用法就是存储用户的首选项。例如，如果用户指明不喜欢查看图形，就可以将该信息存储在 Session 对象中。注意 会话状态仅在支持 cookie 的浏览器中保留。
>
> **Django项目默认启用Session。**

### Session的理解:

- 广义来讲: session是一种会话机制, 用于记录多次http请求之间的关系,关系就是状态数据,比如登录状态.
- 狭义来讲: session是一种会话数据, 记录的状态数据, 比如登录之后记录的user_id等.

### 关闭

> 在settings中的MIDDLEWARE中对session进行开启和关闭注释掉即关闭



## 2.session存储方式

>在settings.py文件中，可以设置session数据的存储方式.
>session可以保存在数据库、本地缓存( 程序的运行内存中, 全局变量)、文件、redis等

### 2.1数据库

存储在数据库中，如下设置可以写，也可以不写，**这是默认存储方式**。
```
# 如果是存放数据库, 一般以db结尾
SESSION_ENGINE='django.contrib.sessions.backends.db'
```
> 如果存储在数据库中需要在settings中INSTALLED_APPS中添加django.contrib.sessions 默认已经添加.
> 表结构有三个数据: 键 值 过期时间.

### 2.2本地缓存

存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快。

```
# 如果是存放在本地缓存, 一般以cache结尾
SESSION_ENGINE='django.contrib.sessions.backends.cache'
```

其中,本地缓存会出现问题: 因为是存放在本地的内存中,所以会出现在脱机情况下出现的跨机访问问题:
> 例如:
```
我们这里可以看到: 有两台服务器存储的有session数据, 前面由nginx负责管理访问机制,有可能现在的访问方式是轮询形式, 那么意味着第一次用户进入的是上面的服务器,进行了登录操作,我们把他的登录状态保存到了服务器1里面, 随后用户有进行了其他操作, 然后有登陆进入这个服务器,这次轮询到了服务器2里面,但是这里面没有保存登录状态,这样就会造成用户第	二次登录.所以会造成用户跨机的问题.
```

### 2.3 混合存储

优先从本机内存中存取，如果没有则从数据库中存取。

```
# 如果是存放数据库,一般以cached_db结尾
SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
```
### 2.4.Redis

> 在redis中保存session，需要引入第三方扩展，我们可以使用**django-redis**来解决。

**2.4.1安装扩展**

```
pip install django-redis
```

**2.4.2设置全局配置**

在settings.py文件中做如下设置

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 定义django中redis的位置
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            # django使用redis的默认客户端来进行操作.
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 我们定义一个cache(本地缓存来存储信息,cache指定的是redis)
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# 本地的session使用的本地缓存名称是'default', 这个名称就是上面我们配置的caches的名称"default"
SESSION_CACHE_ALIAS = "default"
```

**2.4.3测试**

> urls.py:

```
# url的配置: 
from django.conf.urls import url
from . import views

urlpatterns = [
     # 保存session数据
    url(r'^set_session', views.set_session), 
    # 获取session数据
    url(r'^get_ session', views.get_session),
]
```

> Views.py:

```
# 定义设置session的视图函数
def set_session(request):
     request.session['one'] = '1'
     request.session['two'] = '2'
     request.session['three'] = '3'
     return HttpResponse('保存session数据成功')

# 定义获取session的视图函数
def get_session(request):
      one = request.session.get('one')
      two = request.session.get('two')
      three = request.session.get('three')
      text = 'one=%s, two=%s, three=%s' % (one,two,three)
      return HttpResponse(text)
```
演示效果:
我们可以打开redis来查看存储的信息:

```
开启redis服务器:
redis-server
开启redis服务端:
redis-cli
select 1
keys *
```



## 3 Session操作

> 通过HttpRequest对象的session属性进行会话的读写操作。
3.1 以键值对的格式写session。
```
request.session['键']=值
例如: 
request.session['one'] = '1'
```
3.2 根据键读取值。
```
request.session.get('键')
例如: 
one = request.session.get('one')
```
3.3 清除所有session，在存储中删除值部分。
```
request.session.clear()
```
3.4 清除session数据，在存储中删除session的整条数据。
```
request.session.flush()
```
3.5 删除session中的指定键及值，在存储中只删除某个键及对应的值。
```
del request.session['键']
```
3.6 设置session的有效期
```
request.session.set_expiry(value)
```

>如果value是一个整数，session将在value秒没有活动后过期。
如果value为0，那么用户session的Cookie将在用户的浏览器关闭时过期。
如果value为None，那么session有效期将采用系统默认值，**默认为两周**，可以通过在settings.py中设置**SESSION_COOKIE_AGE**来设置全局默认值。其中 **SESSION_COOKIE_AGE**的单位是以秒为单位的.











