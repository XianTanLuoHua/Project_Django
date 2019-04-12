# Django

## 1.特点:

### 1.1.重量级框架

	提供项目工程管理的自动化脚本工具( 脚手架工具 )
	数据库ORM支持（对象关系映射，英语：Object Relational Mapping）
	模板
	表单
	Admin管理站点
	文件管理
	认证权限
	session机制
	缓存

### 1.2.mtv模式

 **有一种程序设计模式叫 *MVC*, 其核心思想是*分工、解耦，让不同的代码块之间降低耦合，增强代码的可扩展性和可移植性*，实现向后兼容。**

	MVC的全拼为**Model-View-Controller**，最早由TrygveReenskaug在1978年提出，是施乐帕罗奥多研究中心(Xerox PARC)在20世纪80年代为程序语言Smalltalk发明的一种软件设计模式，是为了将传统的输入（input）、处理（processing）、输出（output）任务运用到图形化用户交互模型中而设计的。
	
	随着标准输入输出设备的出现，开发人员只需要将精力集中在业务逻辑的分析与实现上。
	
	后来被推荐为Oracle旗下Sun公司Java EE平台的设计模式，并且受到越来越多的使用ColdFusion和PHP的开发者的欢迎。
	
	现在虽然不再使用原来的分工方式，但是这种分工的思想被沿用下来，广泛应用于软件工程中，是一种典型并且应用广泛的软件架构模式。
	
	后来，MVC的思想被应用在了Ｗeb开发方面，被称为Ｗeb MVC框架。
##### 1.2.1Django使用的MVT模式说明

	M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
	V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。
	T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。
## 2.环境搭建_1.0

### 1. 创建虚拟环境

> 和我们学习flask一样, 我们需要使用 virtualenvwrapper 帮我们创建一个单独的虚拟环境, 搭建项目.

```
mkvirtualenv django_env -p python3
```

	mkvirtualenv : 创建一个新的虚拟环境
	django_env : 创建的新虚拟环境名称, 这个名称可以随意制定, 自己能看懂即可
	-p : 制定使用的python解释器版本
	python3 : 我们这里使用 python3 的解释器.
### 2. 安装Django

```
pip install django==1.11.11
```

### 3. 复习虚拟环境和pip的命令

```
# 虚拟环境:

# 创建虚拟环境
mkvirtualenv 
# 删除虚拟环境
rmvirtualenv  
# 进入虚拟环境、查看所有虚拟环境
workon  
# 退出虚拟环境
deactivate  



# pip:

# 安装依赖包
pip install  
# 卸载依赖包
pip uninstall  
# 查看已安装的依赖包
pip list  
# 冻结当前环境的依赖包
pip freeze
```

### 4.创建工程的命令为：

```
# 生成一个django项目工程的使用方式: 

django-admin startproject 工程名称
```

## 3.环境搭建_2.0

**pycharm新建django环境create后,pycharm下方terminal控制台点开已经是默认进入虚拟环境了,由于新建的django环境pycharm给我们默认安装的django2.2,所以我们需要手动下载1.11.11版本**

	pip install Django==1.11.11

**由于2.2和1.11.11版本不同,创建之后需要在路由文件'urls'文件中改变一下导入方式**

```
from django.conf.urls import url,include
```

## 4.项目中各个文件的作用

	与项目同名的目录，此处为demo。
	**settings.py** 是项目的整体配置文件。
	**urls.py** 是项目的URL配置文件。
	**wsgi.py** 是项目与WSGI兼容的Web服务器入口。
	**manage.py** 是项目管理文件，通过它管理项目。

## 5. 运行开发服务器

**在开发阶段，为了能够快速预览到开发的效果，django提供了一个纯python编写的轻量级web服务器，仅在开发阶段使用。**

1.我们可以通过命令行进入刚刚创建的项目目录中:

```
# 进入创建的demo工程目录
cd demo
```

2.运行服务器命令如下：

```
我们可以运行django提供的建议运行服务器来运行我们添加的代码
python manage.py runserver IP地址:端口


如果IP地址和端口号不想指定,可以使用系统默认提供的127.0.0.1的ip地址和8000的端口号
上式就可以简写成: 
python manage.py runserver
```
