# 插播，数组的复制
import numpy as np

x = np.array([1, 2, 3, 4])
y = x # 这是一个浅拷贝
y[0] = 100
print(y, x)
print(id(y), id(x))

y = x.copy() # 深拷贝
y[0] = 200
print(y, x)
print(id(y), id(x))

y1 = x[1:4]
print(y1)
print(id(y1), id(x))

y2 = x.reshape(2, 2)
print(y2)
print(id(y2), id(x))

y3 = np.sort(x)
print(y3)
print(id(y3), id(x))


np.random.seed(12)
a = np.random.randint(0, 31, [20, 4])
h, mm = a.shape
i = np.random.randint(0, h, 8)
j = np.random.randint(0, mm, 8)
a = a.astype(np.float64)
a[i, j] = np.nan

# 用0填充a中nan，并计算列均值
yy = a.copy()
# yy[i, j] = 0
# print(yy)
yy[np.isnan(yy)] = 0
print(yy)
print(np.mean(yy, axis=0))

# 用列均值填充a中nan
t1 = np.nanmean(a, axis=0).round(2)
a1 = a.copy()
print(a1[np.isnan(a1)])
print(a1.shape[1])
for i in range(a1.shape[1]):
    a1[:, i][np.isnan(a1[:, i])] = t1[i]
print(a1)
print(np.mean(a1, axis=0).round(2))
print("-"*60)

# 将a中0列作为主关键字，1列作为次关键字， 对a进行排序
print(a)
a = a[np.argsort(a, axis=0)[:, 1]]
print("-"*60)
print(a)
a = a[np.argsort(a, axis=0, kind="mergesort")[:, 0]]
print("-"*60)
print(a)

# index1 = np.argsort(a[:, 1])
# bb = a[index1]
# index2 = np.argsort(bb[:, 0])
# print(bb[index2])
