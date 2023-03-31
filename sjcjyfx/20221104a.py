import math
import numpy as np
import pandas as pd

# 3、创建数组及数组属性 np.arange(起点，终点，步长  )左闭右开
a4 = np.arange(12).reshape(3, 4) #二维
print(a4)
print("维度：", a4.ndim)
print("形状：", a4.shape)
print("大小：", a4.size)
print("类型：", a4.dtype)
print("-"*60)
a5 = np.arange(24).reshape(2, 3, 4) #三维列是最低维，维度是0，3行是中间维，维度是1；2个卖弄是最高维，维度是2
print(a5)
print("维度：", a5.ndim)
print("形状：", a5.shape)
print("大小：", a5.size)
print("类型：", a5.dtype)

print(type(a5))
print("-"*60)
# 4、等分数组 np.linspace(起点，终点，份数) 左闭右闭
a = np.linspace(0,1,11)
print(a)
print("-"*60)
# 5、特殊数组
# 全0数组
a = np.zeros((3,4)) #元组，列表皆可
print(a)
print("-"*60)
# 全1数组
a = np.ones([5,6])
print(a)
print("-"*60)
# 对角线数组
a = np.eye(5)
print(a)
print("-"*60)
# 二、数组的特性
# 数组的数据类型，在创建之初就已经确定，无法修改
arr = np.array([3, 4, 5])
print(arr.dtype)
print("-"*60)

arr[1] = 7
print(arr)
print("-"*60)

arr = np.array([3.0, 4, 5])
print(arr.dtype)
print("-"*60)

arr = np.array([3, 4, 5])# 强制类型转换不能修改arr本身
arr = np.float64(arr)
arr[1] = 7.8
print(arr.dtype)
print(arr)
print("-"*60)

arr = np.array([3, 4, 5])
arr = arr.astype(np.float64) # astype不能修改arr本身
print(arr)
print("-"*60)

# 三、随机子模块random
# 1、生成无约束随机数（0-1）之间
print(np.random.random(10)) # 生成10个无约束随机值
print(np.random.random([3,4])) # 生成3行4列无约束随机值
print("-"*60)

# 2、生成均匀分布随机数（0-1）之间
print(np.random.rand(10)) # 生成10个均匀分布随机值
print(np.random.rand(3,4)) # 生成3行4列均匀分布随机值
print("-"*60)

# 3、生成正态分布随机数（-2.58~2.58）之间
print(np.random.randn(10)) # 生成10个正态分布随机值
print(np.random.randn(3,4)) # 生成3行4列正态分布随机值
print("-"*60)

# 如何证明生成的随机数组是均匀分布还是正态分布
a = np.random.rand(100000)
a1 = np.random.randn(100000)
print(a.mean(), a1.mean())
print("-"*60)

# 4、随机种子（伪随机数）
np.random.seed(1) # 指定随机种子
print(np.random.rand(5))
print("-"*60)

# 5、生成随机整数数组
np.random.seed(1)
print(np.random.randint(0, 100, 10))
print("-"*60)

np.random.seed(1)
print(np.random.randint(0, 100, [3, 4]))
print("-"*60)

# 6、打乱顺序 np.random.shuffle(a)
a = np.arange(1,13).reshape(3, 4)
np.random.shuffle(a) # shuffle会改变数组本身
print(a)
print("-"*60)

# 6、改进
a = np.arange(1,13)
np.random.shuffle(a)
a = a.reshape(3,4)
print(a)
print("-"*60)

# 验证：shuffle只能打乱高维度
a = np.arange(1,61).reshape(3, 4, 5)
print("原始数组：", a)
np.random.shuffle(a)
print("打乱后：", a)
print("-"*60)

# 7、按照指定概率抽取随机数，组成数组np.random.choice(抽取范围，数组的尺寸，指定的概率)
# 抽取范围可以是列表，可以是整数;指定的概率：针对范围，它必须和范围具有相同的长度，概率的和必须为1，如果省略，则表示等概率
print(np.random.choice(100, size=10)) # [0,100)范围内，等概率抽取10个数据
print(np.random.choice(100, size=[3, 4])) # [0,100)范围内，等概率抽取12个数据,组成4行5列数组
print("-"*60)

# 思考：按照等概率，模拟实现投掷硬币的程序
res = np.random.choice([0, 1], size=1000, p=[0.5, 0.5])
print(res)
print(pd.value_counts(res))
print("-"*60)















