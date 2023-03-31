import math
import numpy as np
import pandas as pd


# 一、数组的运算
# 1、算数运算
a = np.array([1, 2, 3, 4])
b = np.array([0.1, 0.2, 0.3, 0.4])
c = np.array([True, True, False, False])
print(a//2) # 除法运算
print(a**2) # 乘方运算
print(~a) # 加一取反
print("-"*60)

# 2、关系和逻辑运算
print(a > 2)
# print(a > b | a > 2)
# print(a > b & a > 2)
print("-"*60)

# 二、数据的简单统计功能
# 1、改变数组形状
a1 = np.arange(1, 25)
a1 = a1.reshape(3, 8) # 不改变数组本身
print(a1)
a1.shape = 2, 12
print(a1)
a1.shape = (2, 3, 4)
print(a1)
print(a1.sum())
print(np.sum(a1))
print(np.sum(a1,axis=0)) # 列
print(np.sum(a1,axis=1)) # 行求和
print("-"*60)

# mean、max、min、median、var(方差)







