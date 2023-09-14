# numpy
import numpy as np

a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose())
# 支持嵌套切片
print(a[:2:1, 1])