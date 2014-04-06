from . import array
from .array import *

from . import helper
from .helper import *

def rand(d0,d1=None,d2=None,d3=None,dtype='float32'):
    dims = getdims((d0,d1,d2,d3))
    ty = getty(dtype)

    if (dims == 1):
        res = ndarray((d0,))
        res.ptr = libaf.randu(d0,  1,  1,  1, ty)
    elif (dims == 2):
        res = ndarray((d0, d1))
        res.ptr = libaf.randu(d1, d0,  1,  1, ty)
    elif (dims == 3):
        res = ndarray((d0, d1, d2))
        res.ptr = libaf.randu(d2, d1, d0,  1, ty)
    else:
        res = ndarray((d0, d2, d2, d3))
        res.ptr = libaf.randu(d3, d2, d1, d0, ty)

    if (res.ptr == 0):
        raise Exception("Failure in rand")

    return res

def randn(d0,d1=None,d2=None,d3=None,dtype='float32'):
    dims = getdims((d0,d1,d2,d3))
    ty = getty(dtype)

    if (dims == 1):
        res = ndarray((d0,))
        res.ptr = libaf.randn(d0,  1,  1,  1, ty)
    elif (dims == 2):
        res = ndarray((d0, d1))
        res.ptr = libaf.randn(d1, d0,  1,  1, ty)
    elif (dims == 3):
        res = ndarray((d0, d1, d2))
        res.ptr = libaf.randn(d2, d1, d0,  1, ty)
    else:
        res = ndarray((d0, d2, d2, d3))
        res.ptr = libaf.randn(d3, d2, d1, d0, ty)

    if (res.ptr == 0):
        raise Exception("Failure in randn")

    return res
