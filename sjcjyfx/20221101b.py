x = [9, 2, 6, 8, 3, 5, 0, 4, 7, 1]


# 选择法
for i in range(len(x)):
    for j in range(i,len(x)):
        if x[j] < x[i]:
            m = x[i]
            x[i] = x[j]
            x[j] = m
print(x)

x = [9, 2, 6, 8, 3, 5, 0, 4, 7, 1]
# 冒泡排序
for i in range(0,len(x)):
    for j in range(0,len(x)):
        if x[i] < x[j]:
            maxn = x[i]
            x[i] = x[j]
            x[j] = maxn
print(x)