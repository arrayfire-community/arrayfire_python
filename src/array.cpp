#include <stdio.h>
#include <arrayfire.h>
#include <af/utils.h>

using namespace af;

extern "C" void info()
{
    af::info();
    fflush(stdout);
}

extern "C" long create_array(int d0, int d1,
                             int d2, int d3,
                             void *data, int ty)
{
    array *arr;
    try {
        arr = new array();
        if (ty == 0) {
            *arr = array(d0, d1, d2, d3,
                         (float *)data);
        } else if (ty == 1) {
            *arr = array(d0, d1, d2, d3,
                         (double *)data);
        } else {
            throw af::exception("unsupported type");
        }
        return (long)(arr);
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}

extern "C" int get_num_elements(long a)
{
    try {
        array *arr = new array();
        arr = (array *)a;
        return arr->elements();
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}

extern "C" int copy_to_np_buffer(void *ptr, long a)
{
    try {
        array *arr = (array *)a;
        arr->host((void *)ptr);
        return 1;
    } catch (af::exception &ae) {
        printf("%s\n", ae.what());
        return 0;
    }
}
