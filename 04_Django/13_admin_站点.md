# 1.使用Admin站点

> 假设我们要设计一个新闻网站，我们需要编写展示给用户的页面，网页上展示的新闻信息是从哪里来的呢？**是从数据库中查找到新闻的信息，然后把它展示在页面上**。但是我们的网站上的新闻每天都要更新，这就意味着对数据库的增、删、改、查操作，那么我们需要每天写sql语句操作数据库吗? 如果这样的话，是不是非常繁琐，所以我们可以设计一个页面，通过对这个页面的操作来实现对新闻数据库的增删改查操作。那么问题来了，老板说我们需要在建立一个新网站，是不是还要设计一个页面来实现对新网站数据库的增删改查操作，但是这样的页面具有一个很大的重复性，那有没有一种方法能够让我们很快的生成管理数据库表的页面呢？**有，那就是我们接下来要给大家讲的Django的后台管理**。Django能够根据定义的模型类自动地生成管理页面。

## 1. 管理界面本地化

> 在settings.py中设置语言和时区

```
LANGUAGE_CODE = 'zh-hans' # 使用中国语言
TIME_ZONE = 'Asia/Shanghai' # 使用中国上海时间
```

## 2. 生成迁移表

	python manage.py makemigrations (可能需要输入app的名称)
	python manage.py migrate (可能需要输入app的名称)

## 3. 创建超级管理员

> 创建管理员的命令如下，按提示输入用户名、邮箱、密码。

```
python manage.py createsuperuser
```

## 4. 打开redis服务器

## 5. 在终端中输入 redis-server

> 打开浏览器，在地址栏中输入如下地址后回车。

```
http://127.0.0.1:8000/admin/
```

## 3 注册模型类

> 登录后台管理后，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，并进行增删改查操作。

打开booktest/admin.py文件，编写如下代码：

```
from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
```

到浏览器中刷新页面，可以看到模型类BookInfo和HeroInfo的管理了

## 4 定义与使用Admin管理类

Django提供的Admin站点的展示效果可以通过自定义**ModelAdmin**类来进行控制。

定义管理类需要继承自**admin.ModelAdmin**类，如下

```
from django.contrib import admin

class BookInfoAdmin(admin.ModelAdmin):
    pass
```

使用管理类有两种方式：

- 注册参数

  ```
    admin.site.register(BookInfo,BookInfoAdmin)
  ```

- 装饰器

  ```
    @admin.register(BookInfo)
    class BookInfoAdmin(admin.ModelAdmin):
        pass
  ```

## 5. 调整页面显示

####  1 页大小

每页中显示多少条数据，默认为每页显示100条数据，属性如下：

```
# 该字段决定每页展示行数的多少

list_per_page=100
```

1）打开booktest/admin.py文件，修改AreaAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    # 每页展示两行
    list_per_page = 2
```

#### 2 列表中的列

属性如下：

```
# 决定列表页展示的内容:

list_display=[模型字段1,模型字段2,...]
```

1）打开booktest/admin.py文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    # 该列表页展示 id 和 btitle, 其他的不展示
    list_display = ['id','btitle']
```

####  3 将方法作为列

> 列可以是**模型字段**，还可以是**模型方法**
>
> 如果是模型方法, 则要求方法有返回值。

例如:

1）打开 booktest / models.py 文件，修改BookInfo类如下：

```
class BookInfo(models.Model):
    ...

    # 定义一个模型方法, 展示到admin站点中:
    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')

    # short_description字段可以设置在admin站点中的名称.
    pub_date.short_description = '发布日期'
```

2）打开 booktest / admin.py 文件，修改BookInfoAdmin类如下：

```
class BookInfoAdmin(admin.ModelAdmin):
    # 把models文件中定义的函数名,添加到列表中.
    list_display = ['id','btitle','pub_date']
```

#### 注意:

方法列是不能排序的，如果需要排序需要为方法指定排序依据。

```
# 指定模型方法的排序依据:

admin_order_field=模型类字段
```

例如:

1）打开booktest/models.py文件，修改BookInfo类如下：

```
class BookInfo(models.Model):
    ...
    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')

    pub_date.short_description = '发布日期'
    # 在刚刚的代码下面添加该方法的排序依据: 依照bpub_date来进行排序
    pub_date.admin_order_field = 'bpub_date'
```

#### 4 关联对象

无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员。

1）打开booktest/models.py文件，修改HeroInfo类如下：

```
class HeroInfo(models.Model):
    ...
    # 也可以在HeroInfo中定义一个函数,进行展示:
    def read(self):
        return self.hbook.bread
    # 该函数在admin站点的展示名称: '图书阅读量'
    read.short_description = '图书阅读量'
```

2）打开booktest/admin.py文件，修改HeroInfoAdmin类如下：

```
class HeroInfoAdmin(admin.ModelAdmin):
    # 把上面定义的函数名添加到列表中: 
    list_display = ['id', 'hname', 'hbook', 'read']
```

#### 5 右侧栏过滤器

属性如下，只能接收字段，会将对应字段的值列出来，用于快速过滤。一般用于有重复值的字段。

```
# 该字段决定了右侧是否有过滤器, 以及按照哪些内容进行过滤: 

list_filter=[]
```

1）打开booktest/admin.py文件，修改HeroInfoAdmin类如下：

```
class HeroInfoAdmin(admin.ModelAdmin):
       # 依照以下字段进行过滤: hbook 和 hgender
    list_filter = ['hbook', 'hgender']
```

 6 搜索框

属性如下，用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。

```
# 可以在当前页面的最上方添加一个搜索框

search_fields=[]
```

1）打开booktest/admin.py文件，修改HeroInfoAdmin类如下：

```
class HeroInfoAdmin(admin.ModelAdmin):
    # 在页面最上面添加一个搜索框: 按照hname进行搜索
    search_fields = ['hname']
```

## 6.调整站点信息

在booktest/admin.py文件中添加一下信息

```
from django.contrib import admin

admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'
```

