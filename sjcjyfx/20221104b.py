import math
import numpy as np
import pandas as pd

x = np.random.choice(['一等奖', '二等奖', '三等奖', '谢谢参与'], size=100, p=[0.03, 0.05, 0.08, 0.84])
print(x)
y = pd.value_counts(x)
print(y)
print('一等奖:'+str(y[3]/100))
print('二等奖:'+str(y[2]/100))
print('三等奖:'+str(y[1]/100))
print('谢谢参与:'+str(y[0]/100))
print(pd.value_counts('一等奖')/100)