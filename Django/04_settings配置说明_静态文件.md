# 配置文件settings.py

## 1.BASE_DIR

**当前工程的根目录，Django会依此来定位工程内的相关文件，我们也可以使用该参数来构造文件路径。**

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


	`___file___` : 可以理解为当前的文件
	os.path.abspath ( 文件 ) : 获取这个文件的绝对路径
	os.path.dirname( 路径 ) : 获取这个路径的上一级路径, 例如:
	os.path.dirname( 路径 ) : 再次获取这个路径的下一级路径.
	这样获取到的 BASE_DIR 其实就是当前项目的根目录.

##  2.DEBUG

**设置是否为调试模式，创建工程后初始值为True，即默认工作在调试模式下。**

**调试模式的作用**：

	1.调试模式下django有个简易服务器在监听当前项目, 如果我们修改代码文件，服务器程序会自动重启, 重新加载修改过的文件 ( 方便开发 )
	2.当Django框架程序出现异常时，向前端(浏览器)显示详细的错误追踪信息
***!注意：部署线上运行的Django不要运行在调式模式下，记得修改DEBUG=False。***

**如果为非调试模式:**

	程序出错后, 浏览器仅显示 500 的错误代码, 不会显示具体的错误信息

## 3.本地语言与时区

```
# LANGUAGE_CODE = 'en-us'   #这里是默认的英语
LANGUAGE_CODE = 'zh-hans'   #这里是设置的中文

# TIME_ZONE = 'UTC'         #默认使用utc时区
TIME_ZONE = 'Asia/Shanghai' #设置使用亚洲上海时区
```

## 4.静态文件

一般用来放js文件、css样式、image等文件

静态文件我们会放在一个静态(static)文件夹中, 统一管理

**STATICFILES_DIRS** : 存放查找静态文件的目录

**STATIC_URL** : 访问静态文件的URL前缀

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static_files') #在上方base_dir已经得知是当前项目的根目录现在需要做的就是就是使根目录与存放静态文件的文件夹进行拼接得到一个新的路径
]
```

## 5.INSTALLED_APPS列表中工程默认配置的信息