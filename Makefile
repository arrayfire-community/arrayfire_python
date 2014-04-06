AF_PATH?=/opt/arrayfire-2.0
CUDA_PATH?=/usr/local/cuda

ifeq ($(shell uname -m), x86_64)
  LIB:=lib64
else
  LIB:=lib
endif
AF_LIB_PATH=$(AF_PATH)/$(LIB)

AF_CFLAGS  = -I$(AF_PATH)/include
ifeq ($(findstring opencl, $(MAKECMDGOALS)), opencl)
	AF_CFLAGS += -DAFCL -I$(OCL_PATH)/include
	AF=afcl
	EXT=ocl
else
	AF_CFLAGS += -I$(CUDA_PATH)/include
	AF=afcu
	EXT=cuda
endif

AF_PY=afpy
AF_PY_PATH=$(shell pwd)
AF_PY_LIB=$(AF_PY_PATH)/arrayfire/lib$(AF_PY).so
LDFLAGS+=-Wl,-rpath,$(AF_LIB_PATH)

run: $(AF_PY_LIB)
	python examples/np.py
	LD_LIBRARY_PATH=$(AF_PY_PATH)/arrayfire  PYTHONPATH=$(shell `pwd`) python examples/af.py

all: $(AF_PY_LIB)

$(AF_PY_LIB): $(AF_PY_PATH)/src/*.cpp
	g++ -shared -fPIC $^ $(AF_CFLAGS) -L$(AF_LIB_PATH) -l$(AF) -o $@ $(LDFLAGS)

clean:
	rm -f $(AF_PY_LIB)

.PHONY: opencl cuda
