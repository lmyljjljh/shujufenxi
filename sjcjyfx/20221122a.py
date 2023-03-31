# 五、空值np.nan
import numpy as np


print(type(np.nan))

# 1、np.nan不能作比较,无法参与普通运算
print(np.nan == np.nan)

a = np.array([1, 2, 3, np.nan])
print(np.isin(1, a))
print(np.isin(np.nan, a)) # 无法判断np.nan是否存在
print(np.sum(a)) # 含有空值的数组无法参与普通运算
print("-"*60)

# 2、如何定位数组中的空值
a = np.random.randint(0, 20, [3, 5])
a = a.astype(np.float64)
print(a)
a[1][2] = np.nan
a[2][3] = np.nan
print(a)
print(np.isnan(a)) # 判断空值
print(~np.isnan(a)) # 判断非空值

b = np.isnan(a)
print(np.any(b, axis=1))
print(a[np.any(b, axis=1)])
print("-"*60)

# 例：在a中插入全空的列，然后将其索引出来
print(np.insert(a, 5, np.nan, axis=1))
c = np.insert(a, 5, np.nan, axis=1)
print(c[:, np.all(c, axis=0)])
print(np.all(c, axis=0))
print("-"*60)

# 在a中屏蔽有空值的行
# 方法1
print(a[np.all(~np.isnan(a), axis=1)])
print("-"*60)

# 方法2
print(np.sum(a, axis=1))
print(a[np.sum(np.isnan(a), axis=1) == 0])
print("-"*60)

# 练习：生成一个20行4列的二维数组取值[0，30]
np.random.seed(5)
a = np.random.randint(0, 31, [20, 4])
h, mm = a.shape
i = np.random.randint(0, h, 8)
j = np.random.randint(0, mm, 8)
a = a.astype(np.float64)
a[i, j] = np.nan

# 按列算平均值、方差、标准差
print(np.nanmean(a, axis=0))
print(np.nanvar(a, axis=0))
print(np.nanstd(a, axis=0))
print(a)
print("-"*60)
# 按照第一列排序
print(a[np.argsort(a, axis=0)[:, 0]])
print("-"*60)




