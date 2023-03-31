import math
import numpy as np
import pandas as pd

a = np.array([1, 3, 5, 7])
b = np.array([2, 4, 6, 8])
dis = np.sqrt(np.sum(a-b)**2)
print(dis)
print("-"*60)

# 二、数组中的最大值
np.random.seed(5)
a = np.random.randint(0, 21, [3, 5])
print(np.max(a), np.max(a, axis=0), np.max(a, axis=1))
print(np.argmax(a), np.argmax(a, axis=0), np.argmax(a, axis=1))
print("-"*60)

# 三、数组中的排序
# 1、排序使用np.sort()
# 2、函数有返回值，但不修改数组本身
# 3、np.sort()表示对a进行行内排序默认axis=1
# 4、默认取的是最高维度axis=-1，即最高维度->行
# 5、axis取None时，表示打破维度，将数组变为以一维数组排序
# 6、help(np.sort())
np.random.seed(10)
a = np.random.randint(0, 30, [5, 8])
print(np.sort(a))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
print("-"*60)

np.random.seed(5)
a = np.random.randint(0, 30, [3, 4, 6])
print("a:", a)
print("2:", np.sort(a, axis=2))   #等价于np.sort(a)
print("1:", np.sort(a, axis=1))
print("0:", np.sort(a, axis=0))
print("None:", np.sort(a, axis=None))
print("-"*60)


np.random.seed(10)
a = np.random.randint(0, 30, [5, 8])










