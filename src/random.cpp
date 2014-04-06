#include <stdio.h>
#include <arrayfire.h>
#include <af/utils.h>

using namespace af;

extern "C" long randu(int d0, int d1, int d2, int d3, int ty)
{
    try {
        array *arr = new array();
        if (ty == 0) {
            *arr = af::randu(d0, d1, d2, d3);
        } else if (ty == 1) {
            *arr = af::randu(d0, d1, d2, d3, f64);
        }
        return (long)(arr);
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}

extern "C" long randn(int d0, int d1, int d2, int d3, int ty)
{
    try {
        array *arr = new array();
        if (ty == 0) {
            *arr = af::randn(d0, d1, d2, d3);
        } else if (ty == 1) {
            *arr = af::randn(d0, d1, d2, d3, f64);
        }
        return (long)(arr);
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}
