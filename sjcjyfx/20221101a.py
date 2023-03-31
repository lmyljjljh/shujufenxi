import math
import numpy as np
import pandas as pd

# 分10份
n = 10

w = 2*math.pi / n

h = [abs(math.sin(i*w)) for i in range(n)]

# print(h)

mj = w*sum(h)

print(mj)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
minn = min(len(l1),len(l2))
l3 = [l1[i]+l2[i] for i in range(minn)]

l4 = [1, 2, 3, 4]
l5 = [i+j for i, j in zip(l1, l4)]
# print(l5)


# 一、创建数组及数组属性
# 1、创建数组及数组属性
# a1 = np.array([1, 2, 3]) #一维数组
a1 = np.array([[1, 2, 3], [4, 5, 6]])# 二维数组
print(a1)
print("维度：", a1.ndim)
print("形状：", a1.shape)
print("大小：", a1.size)
print("类型：", a1.dtype)

a2 = np.array([[1, 2, 3], [4, 5, "6"]])# 二维数组
print(a2)
print("维度：", a2.ndim)
print("形状：", a2.shape)
print("大小：", a2.size)
print("类型：", a2.dtype)

# 2、创建数组及数组属性
a3 = np.array([[1, 2, 3], [4, 5, 6, 7]])# 二维数组
print(a3)
print("维度：", a3.ndim)
print("形状：", a3.shape)
print("大小：", a3.size)
print("类型：", a3.dtype)

# 3、创建数组及数组属性 np.arange(起点，终点，步长  )左闭右开
a4 = np.arange(12).reshape(3, 4) #二维
print(a4)
print("维度：", a4.ndim)
print("形状：", a4.shape)
print("大小：", a4.size)
print("类型：", a4.dtype)

a5 = np.arange(24).reshape(2, 3, 4) #三维
print(a5)
print("维度：", a5.ndim)
print("形状：", a5.shape)
print("大小：", a5.size)
print("类型：", a5.dtype)

