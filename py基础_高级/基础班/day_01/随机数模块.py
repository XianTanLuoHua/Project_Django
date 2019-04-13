import random
#a = random.randint(6) #没有给开始参数  TypeError: randint() missing 1 required positional argument: 'b'
a = random.randint(1,3) # 取值全范围1,6随机数 左右都看
print(a)