# Git
Git是目前世界上最先进的分布式版本控制系统
## 作用
源代码管理
### 为什么要进行源代码管理?
​	1.方便多人协同开发
	2.方便版本控制
![](/home/xiantanluohua/Desktop/工作区暂存区和仓库区.png)
# git单人本地仓库操作
## 安装git
	sudo apt-get install git
## 创建项目
##### 1.在桌面上创建test文件夹
	mkdir   Desktop/test
##### 2.进入到文件夹内
	cd Desktop/test/
##### 3.初始化文件夹使其变为一个仓库
	git init
##### 4.在仓库内配置个人信息
	git config user.name 'XianTanLuoHua'
	git config user.email '849317537@qq.com'
	不进行配置的话默认使用全局配置全局git配置文件路径：~/.gitconfig
## 查看状态
	git status
	红色表示文件在工作区
	绿色表示文件在暂存区
## 提交
##### 1.提交到暂存区
	git add ./ 表示提交当前项目中所有的文件
	git add login.py 提交指定文件
##### 2.提交到仓库区
	git commit -m '备注描述' 把暂存区内的文件提交到仓库区
	commit会生成一条版本记录,-m后面是版本描述信息

## 查看日志
	git log    查看详细日志
	git reflog 查看简略日志

## 回退版本

#### 方案1

	git reset --hard HEAD^
```HEAD表示当前最新版本
HEAD^表示当前最新版本的前一个版本
HEAD^^表示当前最新版本的前两个版本，以此类推...
HEAD~1表示当前最新版本的前一个版本
HEAD~10表示当前最新版本的前10个版本，以此类推...
```
#### 方案2
	git reset --hard 版本号
**当版本非常多时可选择的方案**
**通过每个版本的版本号回退到指定版本**
![](/home/xiantanluohua/Desktop/回退版本版本号.png)
## 撤销
**只能撤销工作区、暂存区的代码,不能撤销仓库区的代码**
**撤销仓库区的代码就相当于回退版本操作**
#### 撤销工作区代码
添加一段新代码num3 = 30，不add到暂存区，保留在工作区

	git checkout file_name
![](/home/xiantanluohua/Desktop/撤销工作区代码前.png)
![](/home/xiantanluohua/Desktop/撤销工作区代码后.png)
#### 撤销暂存区代码
	第一步将暂存区代码撤销到工作区
		git reset HEAD file_name
	第二步撤销工作区代码
		git checkout file_name
![](/home/xiantanluohua/Desktop/撤销暂存区代码.png)
## 对比版本
##### 对比版本库内与工作区
新加代码num3 = 30，不add到暂存区，保留在工作区

		git diff HEAD -- login.py
![](/home/xiantanluohua/Desktop/对比版本库与工作区.png)
##### 版本库相互对比
新加代码num3 = 30，并add到暂存区

	git diff HEAD HEAD^ -- login.py

![](/home/xiantanluohua/Desktop/对比版本库.png)
## 删除文件

	git rm file_name 
##### 删除后记录删除操作版本

	git commit -m '删除描述'

##### 误删处理
	撤销工作区的修改即可
	git checkout -- file_name


# git管理远程仓库
首次 获取远程仓库的全部文件

	git clone url
把仓库区上传到github

	git push
从远端拉取最近更新

	git pull

