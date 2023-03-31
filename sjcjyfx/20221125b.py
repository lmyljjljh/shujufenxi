import numpy as np
import pandas

x = np.loadtxt(r"D:\Tencent Files\2630639540\FileRecv\iris-150.data", delimiter=",", dtype="str")
print(x)
t1 = x[:, range(x.shape[1]-1)]
# print(t1)
# print(type(t1))
t1 = t1.astype(np.float64)
print(t1)
t2 = t1+10
print(t2)
t3 = t1[:, 1]
print(t3)
t4 = t1[np.argsort(t1, axis=0)[:, 0]]
print(t4)
h, mm = t1.shape
np.random.seed(5)
i = np.random.randint(0, h, 8)
j = np.random.randint(0, mm, 8)
t1[i, j] = np.nan
t5 = t1.copy()
# yy[i, j] = 0
# print(yy)
t5[np.isnan(t5)] = 0
print(t5)
print(np.mean(t5, axis=0))

t6 = np.nanmean(t1, axis=0).round(2)
a1 = t1.copy()
print(a1[np.isnan(a1)])
print(a1.shape[1])
for i in range(a1.shape[1]):
    a1[:, i][np.isnan(a1[:, i])] = t6[i]
print(a1)
print(np.mean(a1, axis=0).round(2))
