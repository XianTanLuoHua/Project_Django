# **redis安装**

#### 	**step1:下载**
	wget <http://download.redis.io/releases/redis-4.0.9.tar.gz>

#### 	**step2:解压**
	tar xzf redis-4.0.9.tar.gz

#### 	**step3:移动文件，放到usr/local⽬录下**
	sudo mv ./redis-4.0.9 /usr/local/redis/

#### 	**step4:进⼊redis⽬录**
	cd /usr/local/redis/

#### 	**step5:生成编译**
	sudo make

#### 	**step6:测试,这段运⾏时间会较⻓**
	sudo make test

#### 	**step7:安装,将redis的命令安装到/usr/local/bin/⽬录**
	sudo make install

#### 	**step8:安装完成后，我们进入目录/usr/local/bin中查看**
	cd /usr/local/bin
	ls -all

#### 	**step9:配置⽂件，移动到/etc/⽬录下**
	配置⽂件⽬录为/usr/local/redis/redis.conf
	sudo cp /usr/local/redis/redis.conf /etc/redis/如果etc目录下没有redis文件需要手动创建



# **redis数据类型与数据库语法**
## **string**
​	**字符串类型是 Redis 中最为基础的数据存储类型，它在 Redis 中是二进制的,这			便意味着该类型可以接受任何格式的数据，如JPEG图像数据或Json对象描述信息等。在Redis中字符串类型的Value最多可以容纳的数据长度是512M。**

##### 	*保存设置键值*
	set name xiaoming	设置name的值为xiaoming
##### 	*保存设置多个键值*
	mset name xiaoming age 18 gender boy	设置name的值为xiaoming,age的值为18......
##### 	*设置键值时效*
	设置存在时效的键值
		setex name 20 xiaoming	设置name的值为xiaoming,且在20s后清除
	查询时效
		ttl name    查询name的时效
##### 	*精准查找*
	get name	查询指定的name的值
	mget name age gender ......    查询多个指定的值
##### 	*范围查找*
	keys *	查找数据库中所有的keys
	keys 'a*'    查询数据库中以开头的	
	keys '\*a\*'    查询数据库中包含a的
##### 	*追加字符*
	append name ming	给指定name的值追加指定的字符
##### 	*删除*
	del name    删除指定的key

##### *查询是否存在*
	exists name    查询键值是否存在  0 不存在    1 存在

## **list**
​	**列表的元素类型为string**
	**按照插⼊顺序排序**
##### *设置和增加*

	lpush name xiaoming xiaohua daliu    从左边设置或者追加name为list 且内部的值为xiaoming xiaohua......
	rpush 从右边开始设置或追加

##### *查找* 
	lrange name 0 -1    查找指定list 内的元素  以0开始 以-1的位置结束
##### *插入*
	linsert name before/after xiaoming liudana    从名字为name的list中的xiaoming的前方或者后方插入指定的值为liudana    before从...之前    after从...之后
##### *修改*
	lset name 1 liuying    修改name这个list中下标为1的值为liuying
##### *删除*
	lrem name 0 xiaoming    删除name这个list中所有为xiaoming的值 0删除所有,2删除两次,-1从后往前删除一次

## **hash**
​	**hash⽤于存储对象，对象的结构为属性、值**
	**值的类型为string**

##### *设置对象以及键值*
	hset stu1 name xiaoming    设置stu1的属性name的值为xiaoming
	hset stu1 name xiaoming age 18 gender boy    设置stu1的属性name的值为xiaoming,age的值为	18,gender为boy
##### *获取*
	het stu1 age    得到stu1对象中属性age的值
	hmset stu1 age name gender 得到stu1对象中多个属性
	hkeys stu1    得到stu1中所有的属性名
##### *删除指定属性*
	hdel stu1 age    删除stu1中的age属性

## **set**
​	**⽆序集合**
	**元素为string类型**
	**元素具有唯⼀性，不重复**
	**说明：对于集合没有修改操作**

##### *设置*
	sadd stu1 xiaoming liuying    设置一个集合为stu1,值为xiaoming liuying
##### *查询*
	smembers key    查询集合内所有的值
##### *删除*
	srem sut1 v1 v2    删除指定set 中的value

## **zset**
​	**sorted set，有序集合**
	**元素为string类型**
	**元素具有唯⼀性，不重复**
	**每个元素都会关联⼀个double类型的score，表示权重，通过权重将元素从⼩到⼤排序**
	**说明：没有修改操作**

##### *设置*

	zadd info 3 san 4 si 4 xiaosi    设置一个info为zset 权重3的为san,权重4的为si 权重4的为xiaosi
##### *查询*
	zrange info 0 -1    查询指定zset 的内容 查询范围从0开始到最后一个结束
	zrangebyscore info min max    查询指定的zset内容  按照权重的范围查找,min max为范围
	zscore key value     查找指定的zset中指定值的权重
##### *删除*
	zrem info 权重    删除zset中指定权重的所有的值



