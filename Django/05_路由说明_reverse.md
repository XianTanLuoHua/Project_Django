## 1.路由定义位置

> Django的主要路由信息定义在工程同名目录下的urls.py文件中，该文件是Django解析路由的入口。
> 每个子应用为了保持相对独立，可以在各个子应用中定义属于自己的urls.py来保存该应用的路由。然后用主路由文件包含各应用的子路由数据。

除了上述方式外，也可将工程的全部路由信息都定义在主路由文件中，子应用不再设置urls.py。如：

```
from django.conf.urls import url
from django.contrib import admin
# 导入子应用的视图模块
import users.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加子应用的路由信息,对应所对应的子应用视图方法
    url(r'^users/index/$', users.views.index)
]
```

 **!但是不推荐**



## 2.路由的解析顺序

> Django在接收到一个请求时，从主路由文件中的urlpatterns列表中以由上至下的顺序查找对应路由规则，如果发现规则为include包含，则再进入被包含的urls中的urlpatterns列表由上至下进行查询。

值得关注的**由上至下**的顺序，有可能会使上面的路由屏蔽掉下面的路由，带来非预期结果。例如：

```
urlpatterns = [
    url(r'^say', views.say),
    url(r'^sayhello', views.sayhello),
]
```

即使访问sayhello/路径，预期应该进入sayhello视图执行，但实际优先查找到了say路由规则也与sayhello/路径匹配，实际进入了say视图执行。

####  两种解决方法:

**第一种:**

> 1. 调整书写顺序

```
from django.conf.urls import url

from . import views

urlpatterns = [
    # 1. 调整书写顺序
    url(r'^sayhello', views.sayhello),
    url(r'^say', views.say)
]
```

**第二种:推荐**

> 2.调整正则书写方式:

```
from django.conf.urls import url

from . import views

urlpatterns = [
    # 2.调整正则:
    url(r'^say/$', views.say),
    url(r'^sayhello/$', views.sayhello)
]
```

## 3. 路由命名空间与reverse反解析（逆向）

> 在视图函数中, 我们可以根据reverse进行反解析,获取当前视图函数的路径. 如：

```
# 注意导包路径, 把reverse导入文件,进行反解析
from django.core.urlresolvers import reverse 

def index(request):
    return HttpResponse("hello the world!")

def say(request):
    url = reverse('usersnamespace:indexname')  
    print(url)    # 打印: /users/index/
    return HttpResponse('say')
```

**总路由可以使用namespace='别名'设置别名,子应用路由使用name='别名设置别名'**

	a=reverse(命名空间namespace:路由name) #得到路径

**如果总路由没有设置别名可以通过`reverse(路由name)`得到的路径,**

## 4. 路径结尾斜线`/`的说明

> Django中定义路由时，通常以斜线/结尾，其好处是用户访问不以斜线/结尾的相同路径时，Django会把用户重定向到以斜线/结尾的路径上，而不会返回404不存在。

例如:

```
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
```

用户访问 index 或者 index/ 网址，均能访问到index视图。

<u>***!!!但是,如果没有/,用户会重定向访问两次。***</u>