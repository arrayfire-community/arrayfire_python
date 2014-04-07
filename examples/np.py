#!/usr/bin/python
import numpy as arr

a = arr.random.rand(4,3)
b = arr.random.randn(3,5)
c = arr.dot(a,b)
d = arr.sum(c)
d0 = arr.sum(c, 0)
d1 = arr.sum(c, 1)

print(a)
print(b)
print(c)
print(d)
print(d0)
print(d1)
