# 思考题：在二维数组中寻找与x最接近的元素及下标
import numpy
import numpy as np
np.random.seed(10)
a = np.random.randint(0, 31, [3, 4])

print(a)
print(a-10)
x = a-10
print(np.argmin(x, axis=1))
print(np.argmin(x, axis=0))
