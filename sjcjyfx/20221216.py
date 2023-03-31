import pandas as pd
import numpy as np
# 一、读写文件
# 1、读文件
# pd.read_csv(path,分隔符（默认为逗号），header='infer',encoding='gbk'(读中文时一般用这两种编码'gbk','utf-8'))
t1 = pd.read_csv(r'D:\Tencent Files\2630639540\FileRecv\meal_order_info.txt', sep=' ')
print(t1)
print(t1.head(10))
t2 = pd.read_csv(r'D:\Tencent Files\2630639540\FileRecv\meal_order_info.csv', encoding='gbk')
print(type(t2))

# 2、写文件
# 数据框对象.to_csv(path,encoding,index=0,header=0) index=0 表示不写入行索引，header=0表示不写入列索引
# t2.to_csv(r'D:\111.csv',encoding='gbk')

# 二、时间类型
# 1、时间类型
# Pandas有常用的时间类型和时间函数
# Timestamp：时间戳，是一个时间点，如某年某月某日某时某分某秒
# Timedelta：时间差，时间单位
# to_datetime：将对象转为时间类型
# 读入点单信息
a1 = t2['lock_time']
t2['lock_time'] = pd.to_datetime(a1)
print(t2['lock_time'])

# 对数据框或系列无法直接执行时间型的属性或函数，需要通过dt接口进行
# dt是pandas的时间属性接口，对接的是时间属性（或函数），返回值为浮点型
# 说明： dt.year、dt.month、dt.day、dt.hour、dt.minute、dt.second、dt.week(dt.weekofyear和dt.week一样)
# 分别返回日期的年、月、日(这个月的第几日)、小时、分、秒及一年中的第几周，这些都是时间相关属性。
# dt.weekday（dt.dayofweek一样），返回一周中的星期几，0代表星期一，6代表星期天；
# dt.day_name() 返回星期几的英文；必须带上括号
# dt.dayofyear 返回一年的第几天；
# dt.quarter得到每个日期分别是第几个季度；
# dt.is_month_start和dt.is_month_end判断日期是否是每月的第一天或最后一天，可以将month换成year和quarter相应的判断日期是否是每年或季度的第一天或最后一天；
# dt.is_leap_year 判断是否是闰年
# dt.month_name()  返回月份的英文名称,必须带上括号
# dt.weekofyear和dt.week 逐步弃用，使用时会报警告错，改为： Series.dt.isocalendar().week
# dt.date 获取年月日
# dt.time 获取时分秒


print(t2['lock_time'])
print(t2['lock_time'].dt.day)     # 该月第几天
print(t2['lock_time'].dt.month_name())  # 该月名称
print(t2['lock_time'].dt.date)  # 日期（年月日），改为time，则取时间（时分秒）
print(t2['lock_time'].dt.weekday)  # 得到星期几，0代表星期一，6代表星期天
print(t2['lock_time'].dt.day_name())  # 得到星期几的名称
print(t2['lock_time'].dt.is_leap_year)  # 本年份是否为闰年

# 时间平移
print(t2['lock_time'].dt.year + 1)  # 不推荐
# 时间先前平移一年
print(t2['lock_time'] + pd.Timedelta(days=-365))

# 说明：pd.Timedelta, 表示时间差，其参数有：
# weeks,days,hours,minutes,seconds
a2 = t2['lock_time'][20] - t2['lock_time'][1]
print(a2)
print(a2.days)  # 计算出的时间差，可以提取天数
print(a2.seconds)  # 计算出的时间差，可以提取秒数，无法提取小时和分钟

print(t2[(t2['lock_time'].dt.day == 11.0) | (t2['lock_time'].dt.day == 10.0)]['lock_time'])
# 筛选出周末的订单
print(t2[(t2['lock_time'].dt.weekday == 5.0) | (t2['lock_time'].dt.weekday == 6.0)])

weekends = ['Saturday', 'Sunday']
t2['星期']=t2['lock_time'].dt.day_name()
t2[t2['星期'].isin(weekends)]





