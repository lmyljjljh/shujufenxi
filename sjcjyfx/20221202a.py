# 三、元素的引用
import pandas as pd
import numpy as np

# 1、系列中元素的引用
t1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(t1[3]) # 引用30
print(t1['d']) # 引用40
print(t1[0: 2]) # 引用10，20
print(t1['a': 'c']) # 引用10，20，30，用索引名进行索引时，是左闭右闭
print(t1[['a', 'c']]) # 引用不连续的元素时，需要两层括号


# 2、数据框中元素的引用
t2 = np.arange(10, 130, 10).reshape(3, 4)
t3 = pd.DataFrame(t2, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print(t3)
print(t3['B']) # 单列引用
# print(t3['a']) # 单行引用报错
# print(t3[1]) # 序号引用报错
print(t3[0: 2]) # 行号切片
print(t3['a':'c']) # 行名切片
print(t3['A': 'B']) # 列名切片不报错但是不是列切片不行
# print(t3[1, 2]) print(t3['a', 'c']) # 报错
print(t3[["A", "C"]]) # 访问不连续

# 结论
'''
1、单层括号内可以是：单个列名，行号、行名切片（左闭右闭）；
2、双层括号内，只能是多个列名
'''

# 引用B列，b，c行
print(t3['b':'c']['B']) # 等价于t3['B']['b':'c']
# 引用b,c行，B,D列
print(t3['b': 'c'][["B", "D"]]) # 等价于t3[["B", "D"]]['b': 'c']


# 3、像numpy一样，引用数据框中数据元素
a = np.arange(10, 130, 10).reshape(3, 4)
t4 = pd.DataFrame(a, index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
print(t4.iloc[1, 2]) # 访问1行2列的元素
print(t4.iloc[0:2, 0:3]) # 访问0~2行，0~3列，左闭右开
# aa [[2, 1], [0, 3]]  若aa是数组，表示引用aa[2,0] aa[1,3]两个元素
print(t4.iloc[[2, 1], [0, 3]]) # 表示引用2，1两行及0，3两行

print(t4.loc['b', 'D']) # 访问b行D列元素
print(t4.loc['a': 'b', 'B': 'D']) # 访问ab行，BDCD列，左闭右开
print(t4.loc[[True, True, False], 'A':'C'])











