import numpy as np
a1 = np.arange(20).reshape(4, 5)
print(a1)
print("0:",a1.sum(axis=0))
print("1:",a1.sum(axis=1))
print("*"*60)

a1 = np.arange(60).reshape(3, 4, 5)
print(a1)
print("0:",a1.sum(axis=0))
print("1:",a1.sum(axis=1))
print("2:",a1.sum(axis=2))
print("*"*60)

a1 = np.arange(120).reshape(2, 3, 4, 5)
print(a1)
print("0:",a1.sum(axis=0))
print("1:",a1.sum(axis=1))
print("2:",a1.sum(axis=2))
print("*"*60)

a1 = np.arange(20).reshape(4, 5)
a1 = np.insert(a1, 0, 100, axis=0)
print(a1)
print("*"*60)

a = np.array([1, 2])
b = np.array([3, 4])
dis = np.sqrt(np.sum(((a-b)**2)))
print(dis)
print("*"*60)


# 三、数组的索引
# 1、普通索引
a1 = np.arange(20).reshape(4, 5)
print(a1[2, 3])
print(a1[1:3,2:4])
print(a1[[1, 2], [3, 4]])
print(a1[[1, 3], :])
print(a1[[3, 3, 1]])
print("*"*60)

# 2、逻辑索引
a1 = np.array([2, 1, 4, 3])
print(a1[[False, False, True, True]])
print(a1[a1 > 2])
print("*"*60)
# 例一
a1 = np.arange(12).reshape(3, 4)
print(a1[a1 > 5])
a1[a1 < 5] = 0
print(a1)
print("*"*60)

a1 = np.arange(20).reshape(4, 5)
print(a1)
print(a1[1, (a1[1] <= 5) | (a1[1] >= 8)])
print(a1[np.all(a1 > 5, axis=1)])
print(a1[:, np.any(a1 < 3, axis=0)])
print(a1[np.all((a1 <= 5) | (a1 >= 10), axis=1)])
print("*"*60)

# 存在0全部大于等于3列
print(a1[:, np.any((a1==0) | np.all(a1 >= 3, axis=0), axis= 0)])










