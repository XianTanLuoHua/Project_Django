# 1. 概念



## ORM框架

> O是object，也就**类对象**的意思，R是relation，翻译成中文是关系，也就是关系数据库中**数据表**的意思，M是mapping，是**映射**的意思。在ORM框架中，它帮我们把类和数据表进行了一个映射，可以让我们**通过类和类对象就能操作它所对应的表格中的数据**。ORM框架还有一个功能，它可以**根据我们设计的类自动帮我们生成数据库中的表格**，省去了我们自己建表的过程。

django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作。

**使用django进行数据库开发的步骤如下：**

> 配置数据库连接信息
> 在models.py中定义模型类
> 迁移
> 通过类和对象完成数据增删改查操作

 **我们使用django和MySQL的时候, 会有问题:**

> django中的ORM框架,在和MySQL对接的时候, ORM只认MySQL官方的MySQL-Python这个包.但是这个安装包安装完成之后, 它的扩展名字叫做mysqldb.

> 但是mysqldb这个库只支持python2的版本, 它不支持python3的版本. 如果我们想要在python3中使用, 那么我们使用的不是MySQL-Python, 而是PyMySQL. 但是ORM又只认mysqldb这个扩展名, 所以我们会把PyMySQL的扩展名改为mysqldb.

	ORM -----只认可----->mysqldb这个扩展名.
	MySQL-Python------安装完成后生成的扩展名为:mysqldb-------只支持python2
	PyMySQL-------支持python3 ---------扩展名不是:mysqldb
	PyMySQL------安装完后,转化为: mysqldb



# 2. 配置

> 我们可以看到django项目创建成功之后, settting.py文件中自动配置了数据库的内容, 配置的是sqlite3数据库:

```
DATABASES = {
    'default': {
        # 默认的配置, 使用的是sqlite3数据库.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

**我们这里要使用的是MySQL的数据库, 所以我们这里要进行修改:**



### 2.1 使用**MySQL**数据库首先需要安装驱动程序

> 修改的第一步: 安装MySQL数据库.

```
 pip install PyMySQL
```



### 2.2 在Django的工程同名子目录的**init**.py文件中添加如下语句

> 第二步: 进行转换, 让pymysql的内容转换为mysqldb,以便于ORM能够匹配

```
 # 复制下面的内容, 拷贝到django工程同名子目录中的 init.py 文件中
 # 例如我们项目为: demo, 那就拷贝到demo/demo/init.py中去.

 from pymysql import install_as_MySQLdb
 install_as_MySQLdb()
```

作用是让Django的ORM能以mysqldb的方式来调用PyMySQL



### 2.3 修改**DATABASES**配置信息

> 第三步: 对数据库进行配置: 修改数据库的ip地址,端口号, 用户名等内容.

```
 # 这个文件在原来的settings.py文件中就有, 我们需要用下面的内容替换原来的内容: 

 DATABASES = {
     'default': {
         # 我们这里需要把sqlite3修改为mysql
         'ENGINE': 'django.db.backends.mysql',
         'HOST': '127.0.0.1',  # 数据库主机
         'PORT': 3306,  # 数据库端口
         'USER': 'root',  # 数据库用户名
         'PASSWORD': 'mysql',  # 数据库用户密码
         'NAME': 'django_demo'  # 数据库名字
     }
 }
```



### 2.4.在MySQL中创建数据库

> 进入数据库mysql -uroot -p2233
> 创建数据库: `create database django_demo default charset=utf8;`



# 3. 定义模型类

> 模型类被定义在"应用/models.py"文件中。
> 模型类必须继承自Model类，位于包django.db.models中:
> from django.db import models



## 3.1 定义

**在子应用中models.py中定义模型类**



#### 3.1.1 添加第一张表

```
# 从django.db中到models
from django.db import models

# 定义图书模型类BookInfo
# 注意: 一定要继承自models.Model

class BookInfo(models.Model):

    # 这里定义的属性对应的都是数据库中的字段:
    # 这里定义的时候,可以额外增加字段: 
    #    max_length字符串的最大长度
    # verbose_name在admin站点的名称. default默认值.
    # models.CharField 这个位置指出了当前字段的类型: 
    
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 该类用于指定数据库中的表名.
    
    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle
```

> 在django中定义的属性(对应数据库中的字段),不需要生命是否存在,只要在这里写入都默认是存在的,就算表中没有等程序走起来会自动在表中被创建起来
> 我们可以在属性的小括号中声明额外当前字段的修饰符.例如:最大长度,默认值等.
> django中,定义模型类的时候我们不需要创建主键,django会自动帮我们创建一个逐渐(整形,自增).
> 如果自己想指定一个主键,需要在指定主键的属性后面添加primary_key=true.
> 默认情况下生命的字段都不能为空,如果为空可以添加null=true



#### 3.1.2 添加第二张表

```
#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    # 这个是元组是一个可选项,元组中也是元组, 其中: 

    # 0, 1: 是在数据库中真实存在的值
    # 意味着hgender这个字段在数据库中存储的要么是0,要么是1

    # male, female: 用于显示在admin站点中
    # 类似于: verbose_name
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='名称') 
    # 性别我们使用的是类似于枚举类型来做的:
    # choices: 可选范围,传入的是个元组类型,在上面定义的.
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')  
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息') 
    # 利用ForeignKey这个属性指定hbook这个字段为外键.
    # 第一个参数: 表示外键关联到书籍表
    # 注意: 如果调用外键hbook的话: 返回的是book这个模型对象.
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname
```



#### 3.1.3 数据库表名:

> 模型类中如果未指定表名,django默认以  **小写app应用名_小写模型类名**  为数据库表名,可以用db_table=指定表名



#### 3.1.4 数据库主键

> django会为表创建自动增长的主键列,每个模型只能有一个主键列,如果使用选项设置某属性为主键列后django不会再创建主键列



#### 3.1.5属性命名限制

> 不能是python 的保留关键字
> 不循序使用连续的下划线,会和django的查询方式冲突



## 3.2 字段类型

| 类型             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| AutoField        | 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性 |
| BooleanField     | 布尔字段，值为True或False                                    |
| NullBooleanField | 支持Null、True、False三种值                                  |
| CharField        | 字符串，参数max_length表示最大字符个数                       |
| TextField        | 大文本字段，一般超过4000个字符时使用                         |
| IntegerField     | 整数                                                         |
| DecimalField     | 十进制浮点数， 参数max_digits表示总位数， 参数decimal_places表示小数位数 |
| FloatField       | 浮点数                                                       |
| DateField        | 日期， 参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为False； 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为False; 参数auto_now_add和auto_now是相互排斥的，组合将会发生错误 |
| TimeField        | 时间，参数同DateField                                        |
| DateTimeField    | 日期时间，参数同DateField                                    |
| FileField        | 上传文件字段                                                 |
| ImageField       | 继承于FileField，对上传的内容进行校验，确保是有效的图片      |



## 3.3 字段选项

| 选项        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| null        | 如果为True，表示允许为空，默认值是False (判断是否允许在数据库系统中字段为空) |
| blank       | 如果为True，则该字段允许为空白，默认值是False, 这个和django中的表无关,和表单有关,django自带有表单系统,有时候用户提交的表单数据会允许为空(例如数据库中就有这个字段) 很少使用. |
| db_column   | 字段的名称，如果未指定，则使用属性的名称                     |
| db_index    | 若值为True, 则在表中会为此字段创建索引，默认值是False        |
| default     | 默认                                                         |
| primary_key | 若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用 |
| unique      | 如果为True, 这个字段在表中必须有唯一值，默认值是False        |
**null是数据库范畴的概念，blank是表单验证范畴的**



## 3.4 外键

> 在设置外键时,需要通过on_delete选项表示主表删除数据时,对于外键引用表数据如何处理,在django.db.models中包含了以下可选的常量

**CASCADE**: 级联，删除主表数据时同时一起删除外键表中数据, 级联删除。
**PROTECT** : 保护模式，如果采用该选项，删除的时候，会抛出`ProtectedError`错误。阻止用户的删除.
**SET_NULL** 置空模式，删除的时候，外键字段被设置为空，仅在该字段null=True: 允许为null时可用.
**SET_DEFAULT** : 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
**DO_NOTHING** 不做任何操作，如果数据库前置指明级联性，此选项会抛出**IntegrityError**异常
**SET()** 自定义一个值，该值当然只能是对应的实体了，看一下代码：

> 当删除mymodel对应的user的时候，mymodel不会删除掉，而是找到一个名叫 deleted的user，与之重建关联

```
  from django.conf import settings
  from django.contrib.auth import get_user_model
  from django.db import models

  def get_sentinel_user():
      return get_user_model().objects.get_or_create(username='deleted')[0]

  class MyModel(models.Model):
      user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.SET(get_sentinel_user),
      )
```


# 4. 迁移

> 将模型类同步到数据库中。
> 我们把上面的模型类信息添加到项目中去:



## 4.1 生成迁移文件

```
python manage.py makemigrations apps_name(可能需要输入app的名称)
```


## 4.2 同步到数据库中

```
python manage.py migrate app_name(可能需要输入app的名称)
```


## 4.3 添加测试信息

```
insert into tb_books(btitle,bpub_date,bread,bcomment,is_delete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);
insert into tb_heros(hname,hgender,hbook_id,hcomment,is_delete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);
```



# 5. shell工具

Django的manage工具提供了**shell**命令，帮助我们配置好当前工程的运行环境（如连接好数据库等），以便可以直接在终端中执行测试python语句。
**在pycharm中的terminal控制台通过如下命令进入shell**
```
python manage.py shell
```
**导入两个模型类，以便后续使用**
```
from booktest.models import BookInfo, HeroInfo
```





# 6. 数据库操作



## 6.1 增

> 增加数据有两种方法:
> 1. 创建对象添加数据, 然后调用 save( ) 保存.
> 2. 通过模型类的 create( ) 函数保存.



###  6.1.1 save

通过创建模型类对象，执行对象的save()方法保存到数据库中。

```
>>> from datetime import date
>>> book = BookInfo(
    btitle='西游记',
    bpub_date=date(1988,1,1),
    bread=10,
    bcomment=10
)
>>> book.save()
>>> hero = HeroInfo(
    hname='孙悟空',
    hgender=0,
    hbook=book
)
>>> hero.save()
>>> hero2 = HeroInfo(
    hname='猪八戒',
    hgender=0,
    hbook_id=book.id
)
>>> hero2.save()
```



### 6.1.2 create

```
>>> HeroInfo.objects.create(
    hname='沙悟净',
    hgender=0,
    hbook=book
)
```



## 6.2 查



### 6.2.1 基本查询

基本查询有三种查询方式:
> **get(条件) 按照指定条件查询单一结果,如果不存在则排除模型类.DoesNotExist异常**
> **all() 查询所有的内容**
> **count() 查询所有数量**

```
>>> BookInfo.objects.all()

>>> book = BookInfo.objects.get(btitle='西游记')
>>> book.id
5

>>> BookInfo.objects.get(id=3)

>>> BookInfo.objects.get(pk=3)

>>> BookInfo.objects.get(id=100)
Traceback (most recent call last):
  File "", line 1, in 
  File "/Users/delron/.virtualenv/dj/lib/python3.6/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name
    args, **kwargs)
  File "/Users/delron/.virtualenv/dj/lib/python3.6/site-packages/django/db/models/query.py", line 380, in get
    self.model._meta.object_name
db.models.DoesNotExist: BookInfo matching query does not exist.

>>> BookInfo.objects.count()
6
```



### 6.2.3 过滤查询

**实现SQL中的where功能,包括:**

> filter:过滤多个结果
> exclude:反向查询
> get:过滤单一结果

**这三种方法的使用大同小异**
> 语法:   类名.objects.filter(属性_运算符=值)



#### 6.2.3.1 相等查询 

> exact 

	bookINFO.objects.filter(id__exact=1) 
	简写 bookINFO.objects.filter(id = 1)
	在bookINFO这张表中查找id为1的信息



#### 6.2.3.2 模糊查询

> contains:是否包含

	bookINFO.objects.filter(id__contains = '传') #查询表中 id 存在 '传' 字符的信息

> endswith startswith 以指定字符 结尾 或开头

	bookINFO.objects.filter(id__endswith = '传')  #查询表中以 '传' 字符结尾的信息
	bookINFO.objects.filter(id__startswith = '传')  #查询表中以 '水' 字符开始的信息



#### 6.2.3.3 空查询

> isnull = True / False 是否为空

	bookINFO.objects.filter(btitle__isnull = True) #查询表中btitle这个字段中为空的信息



#### 6.2.3.4 范围查询

> in 是否包含在范围内

	bookINFO.objects.filter(id__in = [1,3,5,7]) #查询id为1或3或7或5的图书



#### 6.2.3.5 比较查询

> gt 大于>
> lt 小于<
> lte 小于等于 <=
> gte 大于等于 >=

	bookINFO.object.filter(id__gt=3) #查找表中字段为 id 中 大于3的信息
	bookINFO.object.filter(id__lte=10) #查找表中的字段为 id 小于或者等于10的信息


#### 6.2.3.6 反向查询

> exclude: 反向查询

	bookINFO.object.exclude(id__=2) #查找表中字段为 id 除了 2 以外的所有的信息.



#### 6.2.3.7 日期查询

> year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。

	bookINFO.object.filter(bpub_data__year = 1980) #查询表中1980年发布的图书
	BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1)) #查询表中1990.1.1之后发布的图书



### 6.2.4 F 对象

> 用来比较两个不同的字段的信息
> 使用时需要导入

	from django.db.models import F

**查询阅读量大于或等于评论量的图书**

```
BookInfo.objects.filter(bread__gte = F('bcomment))
```
**查询阅读量大于两倍评论量的图书**

	BookInfo.objects.filter(bread__gt = F('bcomment) * 2)



### 6.2.5 Q 对象

> 一般我们在Django程序中查询数据库操作都是在QuerySet里进行进行，例如下面代码:

```
 >>> q1 = BookInfo.objects.filter(headline__startswith="What")
 >>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
 >>> q3 = q2.filter(pub_date__gte=datetime.date.today())
```
> 或者将其组合起来，例如:

```
BookInfo.objects.filter(headline__startswith='What').exclude(pub_date__gte=datetime.now()).filter(pub_date__gte=datetime(2005, 1, 1))
```
随着我们的程序越来越复杂，查询的条件也跟着复杂起来，这样简单的通过一个filter()来进行查询的条件将导致我们的查询越来越长。



**Q( )对象就是为了将这些条件组合起来。**

**使用时需要导入**

```
django.db.models import Q
```

```
# 使用Q对象查询: 
q=Q(question_startswith="What")
```

> 这样就生成了一个Q()对象
> 我们可以使用符号 & 或者 | 将多个Q( )对象组合起来传递给filter()，exclude()，get()等函数。
> 当多个Q( )对象组合起来时，Django会自动生成一个新的Q( )。

**例如下面代码就将两个条件组合成了一个**

```
Q(question__startswith = 'Who') | Q(question__startswith = 'What')
```

**使用上述代码可以使用SQL语句这么理解:**
```
WHERE question LIKE 'Who%' OR question LIKE 'What%'
```
#### 另外:

**我们可以在Q()对象的前面使用字符“~”来代表意义“非”，例如下面代码:**

```
Q(question__startswith='Who') | ~Q(pub_date__year=2005)
```

**对应SQL语句可以理解为:**

```
WHERE question like "Who%" OR year(pub_date) !=2005
```

#### 实例

**例：查询阅读量大于20的图书，改写为Q对象如下。**

```
from django.db.models import Q

BookInfo.objects.filter(Q(bread__gt=20))
```

Q对象可以使用 &、| 连接

> & 表示逻辑与
>
> | 表示逻辑或。

**例1：查询阅读量大于20，或编号小于3的图书:**

```
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
```

**例2:**

```
BookInfo.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```

> 上面的代码可以理解为:

```
SELECT * from BookInfo WHERE question LIKE 'Who%'  AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
```

 **Q对象前可以使用~操作符，表示非not。**

> 例：查询编号不等于3的图书。

```
BookInfo.objects.filter(~Q(id=3))
```

### 6.2.6 聚合函数

> 使用 aggregate( ) 过滤器调用聚合函数。
> 聚合函数包括：
> **Avg** 平均
> **Count** 数量
> **Max** 最大
> **Min** 最小
> **Sum** 求和
> 被定义在django.db.models中,引入:

```
from django.db.models import Sum, Avg, Count, Max, Min
```

> 查询图书的总阅读量。

```
# 导入: 
from django.db.models import Sum

# 查询图书的阅读总量
BookInfo.objects.aggregate(Sum('bread'))
```

**注意aggregate的返回值是一个字典类型**

```
  {'属性名__聚合类小写':值}

  如:
  {'bread__sum':3}
```

**使用count时一般不使用aggregate( )过滤器**

例：查询图书总数。

```
# 使用Count时直接调用即可: 
BookInfo.objects.count()
```

注意count函数的返回值是一个数字。

### 6.2.7 排序

使用**order_by**对结果进行排序

```
# 依照阅读量的个数: 从少到多依次排序
# 升序
BookInfo.objects.all().order_by('bread')  

 # 降序
BookInfo.objects.all().order_by('-bread')
```



### 6.2.8 关联查询

#### 6.2.8.1 一对多的访问方式:

> 一对应的是: 模型类对象.
> 多对应的是: 模型类名小写_set

```
使用方式: 

变量 = 模型类.objects.get(属性=某一个)

变量.关联类_set.条件
```

例如:

```
# 获取id=1的书(射雕英雄传)所对应的英雄人物: 

b = BookInfo.objects.get(id=1)  #先得到在bookINFO表中id为1的对象
b.heroinfo_set.all()            #按照外链查找heroinfo中 上方对应的每个信息
								#查找到返回 def __str__(self): 的信息
```

结果:

```
<QuerySet [<HeroInfo: 郭靖>, <HeroInfo: 黄蓉>, <HeroInfo: 黄药师>, <HeroInfo: 欧阳锋>, <HeroInfo: 梅超风>]>
```

#### 6.2.8.2 由多到一的访问方式:

> 多对应的是: 模型类对象
>
> 一对应的是: 模型类中的关系类属性名

```
# 获取id=1的英雄们(射雕英雄传中的), 所在的书籍名称: 

h = HeroInfo.objects.get(id=1)   #得到heroinfo表中id为1的对象
h.hbook                          #根据外链查找所外的表
								 #查找到返回 def __str__(self): 的信息
```

结果:

```
<BookInfo: 射雕英雄传>
```

获取: **一个对象对应的模型类所关联对象的id语法:**

多对应的模型类对象.关联类属性_id

例：

```
# 获取id=1的英雄人物(郭靖), 所对应书籍的id值(主键):

h = HeroInfo.objects.get(id=1)
h.hbook_id
```

结果:

```
1
```



#### 6.2.8.3 关联过滤查询

##### 6.2.8.3.1 第一种:

> 由多模型类条件查询一模型类数据:
>
> 多模型 =====> 一模型

```
语法如下：

关联模型类名小写__属性名__条件运算符=值
```

> **注意：**
>
> 其中: __条件运算符 部分,可以没有.
>
> **如果: __条件运算符 部分没有，则表示等于( = )。**
>
> 这里的都是双下划线, 而不是单下划线, 否则报错.

例如 :

> 查询图书，要求图书英雄为"孙悟空"

```
# 查询图书，要求图书英雄为"孙悟空"

BookInfo.objects.filter(heroinfo__hname='孙悟空')
```

结果:

```
<QuerySet [<BookInfo: 西游记>]>
```

> 查询图书，要求图书中英雄的描述包含"八"

```
# 查询图书，要求图书中英雄的描述包含"八"

BookInfo.objects.filter(heroinfo__hcomment__contains='八')
```

结果:

```
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
```

##### 6.2.8.3.2 第二种:

> **由一模型类条件查询多模型类数据**:

```
语法如下：

一模型类关联属性名__一模型类属性名__条件运算符=值
```

> **注意：如果没有"__运算符"部分，表示等于。**

例如 ：

> 查询书名为“天龙八部”的所有英雄。

```
# 查询书名为“天龙八部”的所有英雄

HeroInfo.objects.filter(hbook__btitle='天龙八部')
```

结果:

```
<QuerySet [<HeroInfo: 乔峰>, <HeroInfo: 段誉>, <HeroInfo: 虚竹>, <HeroInfo: 王语嫣>]>
```

> 查询图书阅读量大于30的所有英雄

```
# 查询图书阅读量大于30的所有英雄

HeroInfo.objects.filter(hbook__bread__gt=30)
```

结果:

```
<QuerySet [<HeroInfo: 乔峰>, <HeroInfo: 段誉>, <HeroInfo: 虚竹>, <HeroInfo: 王语嫣>, <HeroInfo: 胡斐>, <HeroInfo: 苗若兰>, <HeroInfo: 程灵素>, <HeroInfo: 袁紫衣>]>
```

##  6.3 修改
> 修改更新有两种方法:
> save
> update

### 6.3.1 save
**修改模型类对象的属性，然后执行save()方法**

```
hero = HeroInfo.objects.get(hname='猪八戒')
hero.hname = '猪悟能'
hero.save()
```

### 6.3.2 update

**使用模型类.objects.filter().update()**，会返回受影响的行数

```
HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')
```



## 6.4 删除
> 删除有两种方法

### 6.4.1 模型类对象delete

```
hero = HeroInfo.objects.get(id=13)
hero.delete()
```
### 6.4.2 模型类.objects.filter().delete()

```
HeroInfo.objects.filter(id=14).delete()
```



# 7. 查询集 QuerySet



## 7.1 概念

**Django的ORM中存在查询集的概念。**
**查询集，也称查询结果集、QuerySet，表示从数据库中获取的对象集合。**
**当调用如下过滤器方法时，Django会返回查询集（而不是简单的列表）：**
> all( )：返回所有数据。
> filter( )：返回满足条件的数据。
> exclude( )：返回满足条件之外的数据。
> order_by( )：对结果进行排序。

**对查询集可以再次调用过滤器进行过滤，如**

```
BookInfo.objects.filter(bread__gt=30).order_by('bpub_date')
```
也就意味着查询集可以含有零个、一个或多个过滤器。过滤器基于所给的参数限制查询的结果。
**从SQL的角度讲，查询集与select语句等价，过滤器像where、limit、order by子句。**
**判断某一个查询集中是否有数据**：
> exists()：判断查询集中是否有数据，如果有则返回True，没有则返回False。



## 7.2 两大特性



#### 7.2.1惰性执行

> 创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用

例如，当执行如下语句时，并未进行数据库查询，只是创建了一个查询集qs

```
qs = BookInfo.objects.all()
```

继续执行遍历迭代操作后，才真正的进行了数据库的查询

```
for book in qs:
    print(book.btitle)
```

#### 7.2.2缓存

> 使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。

**情况一**：如下是两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载。

```
from booktest.models import BookInfo
[book.id for book in BookInfo.objects.all()]
[book.id for book in BookInfo.objects.all()]
```

**情况二**：经过存储后，可以重用查询集，第二次使用缓存中的数据。

```
qs=BookInfo.objects.all()
[book.id for book in qs]
[book.id for book in qs]
```



## 7.3 限制查询集

> 可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。

**注意：不支持负数索引。**

**对查询集进行切片后返回一个新的查询集，不会立即执行查询。**

> 如果获取一个对象，直接使用[0]，等同于[0:1].get()，但是如果没有数据，[0]引发IndexError异常，[0:1].get()如果没有数据引发DoesNotExist异常。

示例：获取第1、2项，运行查看。

```
qs = BookInfo.objects.all()[0:2]
```