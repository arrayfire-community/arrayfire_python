#include <stdio.h>
#include <arrayfire.h>
#include <af/utils.h>

using namespace af;

extern "C" long matmul(long a, long b)
{
    try {
        array *A = (array *)a;
        array *B = (array *)b;
        array *C = new array();
        *C = af::matmul(*B, *A);
        return (long)(C);
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}

extern "C" double sumAll(long a)
{
    try {
        array *A = (array *)a;
        if (A->type() == f32) {
            return sum<float>(*A);
        } else if (A->type() == f64) {
            return sum<double>(*A);
        }
        throw af::exception("SUM unsupported type");
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}

extern "C" long sum(long a, int dim)
{
    try {
        array *A = (array *)a;
        array *B = new array();
        int ndims = A->numdims();
        *B = sum(*A, ndims - (dim + 1));
        return (long)(B);
        throw af::exception("SUM unsupported type");
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}
