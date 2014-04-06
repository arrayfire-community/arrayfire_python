from . import array
from .array import *

from . import helper
from .helper import *

def dot(A, B):
    res = ndarray(shape=(A.shape[0], B.shape[1]), dtype=A.dtype)
    res.ptr = libaf.matmul(A.ptr, B.ptr)
    if (res.ptr == 0):
        raise Exception("Failure in dot")
    return res

def sum(A, dim=None):
    if dim is None:
        sum_all = libaf.sumAll
        sum_all.restype = c_double
        res = libaf.sumAll(A.ptr)
    else:
        lst = list(A.shape)
        lst[dim] = 1
        shape = strip(lst)
        res = ndarray(shape, dtype=A.dtype)
        res.ptr = libaf.sum(A.ptr, dim)
        if (res.ptr == 0):
            raise Exception("Failure in dot")    
    return res
