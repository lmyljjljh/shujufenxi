import numpy as np


# 数据标准化
x = np.random.randint(1, 30, [20, 4])
print(x)
t1 = x[:, range(x.shape[1]-1)]
# print(t1)
# print(type(t1))
t1 = t1.astype(np.float64)
print(t1)
print("-"*60)
# 归一化
#公式：（data-min)/(max-min)
print(((t1[:, 0] - t1[:, 0].min())/(t1[:, 0].max() - t1[:, 0].min())).round(2))
print("-"*60)

# 对t1整个数组进行归一化（标准化、0-1标准化），生成新的数组t2
t2 = t1.copy()
lines = t1.shape[1] #得到列数
for i in range(lines):
    t2[:, i] = ((t2[:, i] - np.min(t2[:, i]))/(np.max(t2[:, i]) - np.min(t2[:, i])))
t2 = t2.round(2)
print(t2)
print("*"*60)

t5 = t1.copy()
t5 = (t5 - np.min(t1, axis=0))/(np.max(t1, axis=0) - np.min(t1, axis=0))
print(t5.round(2))

# 标准化：中心化 （data-列均值）/列标准差
t3 = t1.copy()
lines1 = t3.shape[1] #得到列数
for i in range(lines1):
    t3[:, i] = (t3[:, i] - np.mean(t1[:, i]))/np.std(t1[:, i])
t3 = t3.round(2)
print(t3)
print("-"*60)


t4 = t1.copy()
t4 = (t4 - np.mean(t1, axis=0)) / np.std(t1, axis=0)
print(t4.round(2))
print("-"*60)



# 读写文件 np.loadtxt("路径", delimiter, dtype, skiprows, usecols)
# delimiter 分割符，默认为空格，delimiter=","
# dtype: 读取数据类型，dtype="np.float64" / "str" / "object"
# skiprows:跳过的行数，skiprows = 1表示跳过1行
# usecols:指定读出的列 usecols=([0, 2, 3]) 注意，不能切片
x = np.loadtxt(r"D:\Tencent Files\2630639540\FileRecv\iris-150.data", delimiter=",", dtype="str")
print(x)
t1 = x[:, range(x.shape[1]-1)]
# print(t1)
# print(type(t1))
t1 = t1.astype(np.float64)
print(t1)
print("-"*60)

# 写文件 np.savetxt("路径+文件名"， 数组名， 写入类型)
# "路径+文件名" 表示写入的地址和文件
# 数组名：写入的数据来源
# 写入类型：格式字符，”%.2f“，”%s“
np.savetxt(r"D:\123.txt", t1, "%.2f")


# 创建系列和数据框
import pandas as pd
import numpy as np

# 1、创建系列
s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s1)

# 2、字典创建系列，字典的键值，不必一样长
s2 = pd.Series({"A": [1, 2, 3, 4], "B": ['a', 'b', 'c']})
print(s2)

# 3、随机数组创建系列，默认行索引
a = np.random.randint(1, 11, 5)
s3 = pd.Series(a)
print(s3)

# 4、创建数据框
df1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": ['a', 'b', 'c', 'd']})
print(df1)

# 普通二维数组创建数据框
df2 = pd.DataFrame([[10, 20, 30, 40], ['a', 'b', 'c'], [3.1, 3.5, 5.7]], index=['A', 'B', 'C'])
print(df2)

# 将上例改为Series
df2 = pd.Series([[10, 20, 30, 40], ['a', 'b', 'c'], [3.1, 3.5, 5.7]], index=['A', 'B', 'C'])
print(df2)

# 创建特殊数据框
# 1、只需要框架，不需要数据
df3 = pd.DataFrame(index=[0, 1, 2, 3], columns=["A", "B", "C", "D"])
print(df3)

# 创建全0的数据框
df4 = pd.DataFrame(0, index=[0, 1, 2, 3], columns=["A", "B", "C", "D"])

# 二、数据框的属性
df = pd.DataFrame(0, index=[0, 1, 2, 3], columns=["A", "B", "C", "D"])
print("值", df.values)
print("空间格式", df.shape)
print("数据类型", df.dtypes)
print("行键", df.index)
print("键值", df.columns)

#查看是否为空值
df.isnull()
#某一列的空值
df["A"].isnull()
# 查看所有值中是否存在空值
df.isnull().any()
# 判断某列是否存在空值
df["A"].isnull().any()
df.isna().any()  #查看原数据表是否存在空值
df3 = df.fillna(method='ffill',axis=0,inplace=False,limit=None,downcast=None)






