from ctypes import *
import numpy as np
from . import helper
from .helper import *

cdll.LoadLibrary("libafpy.so")
libaf = CDLL("libafpy.so")

class ndarray(object):
    """ ArrayFire array """
    def __init__(self,
                 shape=(0,),
                 dtype="float32",
                 data=None):
        self.ptr = 0
        self.dtype = dtype
        if isinstance(data, np.ndarray):
            shape = data.shape
            self.shape = data.shape
            dims = getdims(data.shape)
            ty = getty(data.dtype)
            buf = data.ctypes.data

            if (dims == 1):
                self.ptr = libaf.create_array(shape[0], 
                                              1,  1,  1,
                                              buf, ty)
            elif (dims == 2):
                self.ptr = libaf.create_array(shape[1], shape[0], 
                                              1,  1, buf, ty)
            elif (dims == 3):
                self.ptr = libaf.create_array(shape[2], shape[1],
                                              shape[0], 1, buf, ty)
            else:
                self.ptr = libaf.create_array(shape[3], shape[2],
                                              shape[1], shape[0],
                                              buf, ty)

            if (self.ptr == 0):
                raise Exception("Failed to create arrayfire.ndarray")
        elif (data is None):
            self.shape = shape
        else:
            raise TypeError("Inputs must be numpy arrays")

    def numpy_array(self):
        res = np.zeros(self.shape).astype(self.dtype)
        libaf.copy_to_np_buffer(res.ctypes.data, self.ptr)
        return res

    def __str__(self):
        return str(self.numpy_array())

    def __repr__(self):
        res_str = "ArrayFire ndarray\n" + str(self.numpy_array())
        return res_str

def array(a):
    if isinstance(a, np.ndarray):
        return ndarray(a.shape, a.dtype, a)
    else:
        raise TypeError("Input type not supported")
