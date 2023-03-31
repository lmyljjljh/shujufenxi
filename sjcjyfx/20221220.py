import pandas as pd
import numpy as np

# 分组聚合
data = pd.DataFrame({"company": ['百度', '阿里', '百度', '阿里', '百度', '腾讯', '腾讯', '阿里', '腾讯', '阿里'],
                     'level': ['P7', 'P7', 'P8', 'P5', 'P8', 'P7', 'P8', 'P7', 'P5', 'P6'],
                     "salary": [43000, 24000, 40000, 39000, 8000, 47000, 25000, 16000, 21000, 38000],
                     "age": [25, 34, 49, 42, 28, 23, 45, 21, 34, 29]})

# agg聚合函数，常常和group by连用，agg也可以单独使用
# 数据狂参与agg运算结构还是数据框
print(data.agg(['max', 'mean']))
print(data.agg({'level': ['max', 'min'], 'salary': ['mean', 'std']}))
print(data.agg({'level': ['max', 'min'], 'salary': ['mean', 'std']}).index)
# 求每个公司的工资平均值（推荐

print(data.groupby('company').agg({'salary': 'mean'}))
print(data.groupby('company')['salary'].mean())
# 分组后没有指明聚合字段，则所有能够参与运算的字段均参与聚合
print(data.groupby('company').agg(['mean', 'max']))


# 思考题：求各公司人员，年龄的均方根，并验证
# 均方根：rms          sqrt(sum(x**2)/n)
def f1(x):
    return np.sqrt(sum(x ** 2) / len(x))


print(data.groupby('company').agg({'age': f1}))
# 验证
print(data[data['company'] == '百度'])

# 二、多级分组
# 对每个公司每个层级的工资穷狂进行聚合
print(data.groupby(['company', 'level']).agg({'salary': ['max', 'min', 'median']}))

# 三、练习
# 读入文件meal_order_info.csv
# 按天分组（星期）,求消费的笔数，金额的最大值最小值，金额的总量
t1 = pd.read_csv(r'D:\Tencent Files\2630639540\FileRecv\meal_order_info.csv', encoding='gbk')
print(t1)
a1 = t1['lock_time']
t1['lock_time'] = pd.to_datetime(a1)
t1['日期'] = t1['lock_time'].dt.date
t1['星期'] = t1['lock_time'].dt.isocalendar().week
print(t1)
print(t1.groupby(['星期', '日期']).agg({'info_id': "count", 'expenditure': ['sum', 'max', 'min']}))