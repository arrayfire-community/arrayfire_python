def getdims(shape):
    d = len(shape) - 1
    while shape[d] is None:
        d = d - 1
        if (d == 0): break
    return d + 1

def strip(lst):
    s = 0
    e = len(lst) - 1

    while lst[s] == 1:
        s = s + 1

    while lst[e] == 1:
        e = e - 1
        if (e == 0): break

    if (s == e): return tuple((lst[s],))
    else:        return tuple(lst[s:e])

def getty(dtype):
    if (dtype == 'float32'):
        return 0
    elif (dtype == 'float64'):
        return 1
    else:
        raise TypeError("Support for float dtypes only")
