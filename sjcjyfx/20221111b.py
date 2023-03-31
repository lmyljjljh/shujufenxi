import math
import numpy as np
import pandas as pd
n = 10
x = np.random.randint(0, 50, n)
y = np.random.randint(0, 50, n)
lista = []
listb = []
listc = []
for i in range(n-1):
    for j in range(i+1, n):
        lista.append((x[i]-x[j])*(x[i]-x[j]))
        listb.append((y[i]-y[j])*(y[i]-y[j]))
for i in range(len(lista)):
    listc.append(math.sqrt(lista[i]+listb[i]))
print(listc)
# 2
listd = []
x = np.random.randint(0, 50, [n, 2])

y = np.zeros([n, n])

for i in range(n):
    for j in range(i, n):
        y[i, j] = y[j, i] = np.sqrt(np.sum((x[i]-x[j])**2))
y = y.round(2)
print(y)