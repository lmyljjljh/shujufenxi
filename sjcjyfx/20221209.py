# 三、缺失值处理
import numpy as np
import pandas as pd
a = np.arange(10, 210, 10).reshape(4, 5)
dff = pd.DataFrame(a, columns=['A', 'B', 'C', 'D', 'E'])

# 人为增加几个空值
dff.iloc[0:2, 1:3] = np.nan
dff.iloc[2, 2:5] = np.nan
dff['F'] = np.nan
print(dff)

# 此例不能使用 iloc进行索引
# 找出有空值的行
row_idx = np.any(np.isnan(dff), axis=1)
# 找出有空值的列
col_idx = np.any(np.isnan(dff), axis=0)
print(dff.loc[:, col_idx])
# 找出有空值的行，不含空值的列
print(dff.loc[row_idx, ~col_idx])

# pandas中判断缺失值的方法：df.isnull()  ,  df.notnull()
print(dff.isnull()) # 等价于：pd.isnul(dff)
print(dff.notnull()) # 等价于：pd.notnull(dff)

# 按列统计，每个列的空值个数，sum中轴向为：axis=0
print(dff.isnull().sum())

# 按行统计，每个行的空值个数，sum中轴向为：axis=1
print(dff.isnull().sum(axis=1))

# 查看A，D两列的空值情况
print(dff[['A', 'D']].isnull().sum(axis=0))

# 查看前两行的空值情况
print(dff[0:2].isnull())

print(dff[0:2].isnull().any(axis=0))
print(dff[0:2].isnull().all(axis=0))
print(dff.isnull().all())

# 查看 dff中，存在nan的列名和列
indx = np.any(dff.isnull(), axis=0)
print(dff.loc[:, indx])
print(dff.loc[:, indx].columns) # 含空值的列名

# 四、填充缺失值
a = np.arange(10, 210, 10).reshape(4, 5)
dff = pd.DataFrame(a, columns=['A', 'B', 'C', 'D', 'E'])

# 人为增加几个空值
dff.iloc[0:2, 1:3] = np.nan
dff.iloc[2, 2:5] = np.nan
dff['F'] = np.nan
print(dff)

# 缺失值填充：
# df.fillna(value=None,method=None,axis=None,inplace=Flase,limit=None,...)
# value:填充值
# method：ffill/bfill      用前面或后面的值填充
# axis=0 默认上下行填充，axis=1表示用左右填充

print(dff.fillna(0)) # 0值填充
# 字典填充

# 字典填充，对应列用对应值填充
values = {"A": 10, "C": 20, "F": 30}
print(dff.fillna(values, limit=2)) # 只填充两个

# 邻值填充，可能需要二轮填充

# 用空值所造的下一行元素进行填充
print(dff.fillna(method='bfill', axis=0))

# 用空值所在的左边一个元素进行填充
print(dff.fillna(method='ffill', axis=1))

# 列均值填充本列空值
print(dff.fillna(dff.mean(axis=0)).round(1))

dff1 = dff.fillna(dff.mean(axis=0)).round(1)

# 若均值填充结束,数据框还有空值，说明整列为空，则屏蔽该列
print(dff1.loc[:, dff1.notnull().all()])

# 填充后，删除全空列
print(dff1.drop(columns=dff1.loc[:, dff1.isnull().all()].columns))
# 等价于
print(dff1.drop(columns=dff1.columns[dff1.isnull().all()]))


# 五、数据描述
a = np.arange(10, 210, 10).reshape(4,5)
dff = pd.DataFrame(a, columns=['A', 'B', 'C', 'D', 'E'])

# 人为增加几个空值
dff.iloc[2, 2:4] = np.nan
dff['F'] = np.nan
print(dff)
dff['G'] = ['AAA', 'bbb', 'ccc', 'ddd']
print(dff.describe())
print(dff.describe(include='all'))
print(dff.describe(include=[object])) # 表示对对象类型进行描述



