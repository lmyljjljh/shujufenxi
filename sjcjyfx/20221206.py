import numpy as np
import pandas as pd

a = np.arange(10, 130, 10).reshape(3, 4)
df = pd.DataFrame(a, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print(df)

# 1、数据框追加
df2 = [100, 200, 300, 400] # 由于和原本列的数量对不上，因此新增加4行添加为1列
df3 = df.append(df2, ignore_index=True)
# ignore_index, 默认值为False，不忽略各自的行索引
# 追加时，建议加上ignore_index
print(df3)


# 在数据框中追加行时，最常用的方式（append不修改原始数据框)
df4 = pd.DataFrame([[100, 200, 300, 400]] ) # 双层中括号
df5 = df.append(df4, ignore_index=True)
print(df5)

# 不建议:ignore_index=False
df6 = pd.DataFrame([[100, 200, 300, 400], [500, 600, 700, 800]], columns=df.columns)
df7 = df.append(df6, ignore_index=True)
print(df7)

# df7['a':'e'] #index_index改为False时，可以索引出来，因为行索引分别为a b c0 1
# df7[0:3]
# df7.loc[0,]
# df7[' a':' c'] #index_index改为True后,索引不出来，因为行索引变成了0123 4,不存在a b c了,索引不出来


# 在数据框中增加列，最简洁的方式
# 2、增加列
df['E'] = np.nan
# 改变数据框本身，增加E列df['F']=[4, 5,6]
print(df)

# 在指定位置增加列，更加具体的方式df, insert(loc, col_name, value, allow_duplicates)
# loc:追加的位置
# col_name:新列的名称#value:新列的值
# allow_duplicates:是否允许新列与旧列重名，默认为False
df.insert(4, '地址', ['aaa', ' bbbb', 'cccc'])
print(df)

# 二、数据框删除行列
# df.drop(行列坐标，axis, inplace)#axis 默认为0，表示删除行
# inplace默认为False，表示不修改原始数据框
a = np. arange(10, 210, 10).reshape(4, 5)
df = pd.DataFrame(a, index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])
print(df)


df.drop(['a', 'c'])
df.drop(index=['a', 'c'])
df.drop(columns=['D', 'E'])
print(df)


# 三、缺失值处理
a = np.arange(10, 210, 10).reshape(4, 5)
dff = pd.DataFrame(a,columns=['A', 'B', 'C', 'D', 'E'])
print(dff)
#人为增肌几个空值

dff.iloc[0:2, 1:3] = np.nan
dff.iloc[2, 2:5] = np.nan
dff['F'] = np.nan
print(dff)
# 找出有空值的行
row_idn = np.any(np.isnan(dff), axis=1)
# 找出有空值的列
col_idx = np.any(np.isnan(dff), axis=0)
dff.loc[:, col_idx]
# 找出有空值的行， 不含空值的列
dff.loc[row_idn, ~col_idx]

dff.iloc[[True, True, False, True], :]

# pandas中判断缺失值的方法：df.innull，df.notnull


