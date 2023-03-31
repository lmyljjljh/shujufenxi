import numpy as np

# 四、间接排序
np.random.seed(6)
a = np.random.randint(0, 30, 10)
print("a:", a)
print("sort(a):", np.sort(a))
print("argsort(a):", np.argsort(a))
print("-"*60)

# 1、找出a中第二小的元素和第三大的元素
print("第2小元素，第3大元素:", a[np.argsort(a)[1]], a[np.argsort(a)[4]])

# 2、将数组a降序排列
print("降序argsort():", np.argsort(a)[::-1])

# 3、x = 18找出a中与18最接近的元素及其下标
print("下标：", np.argmin(np.abs(a-18)))
print("元素：", a[np.argmin(np.abs(a-18))])

# 4、将一个二维数组按照某列关键字排序
np.random.seed(10)
a = np.random.randint(0, 30, [5, 8])
print(np.argsort(a, axis=0))
print(a[np.argsort(a, axis=0)[:, 0], :])



# 思考题：在二维数组中寻找与x最接近的元素及下标




