#!/usr/bin/python
import arrayfire as np

a = np.random.rand(4,3)
b = np.random.randn(3,5)
c = np.dot(a,b)
d = np.sum(c)
d0 = np.sum(c, 0)
d1 = np.sum(c, 1)

print(a)
print(b)
print(c)
print(d)
print(d0)
print(d1)
