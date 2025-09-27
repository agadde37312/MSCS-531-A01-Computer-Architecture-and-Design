DLP Examples Package
====================

Contents:
- numpy_vector.py            : Python NumPy vectorized example (array add, timing, plot)
- avx_add.c                  : C program using AVX (256-bit) intrinsics to add float arrays
- avx_makefile               : Makefile to build avx_add.c (gcc/clang with -mavx)
- openmp_reduce.c            : C example using OpenMP to parallelize a loop (reduction)
- openmp_makefile            : Makefile to build openmp_reduce.c (gcc -fopenmp)
- cuda_matmul.cu             : CUDA example for matrix multiplication (simple kernel)
- cuda_makefile              : Makefile to build CUDA example (nvcc)
- plot_helper.py             : Python helper to plot results CSVs
- run_all.sh                 : Script to run Python example, compile C examples (if toolchain present)

Requirements:
- Python 3 with numpy, matplotlib
  pip3 install numpy matplotlib
- For AVX: gcc/clang with AVX support
- For OpenMP: gcc with -fopenmp
- For CUDA: nvcc and CUDA toolkit (optional)

Notes:
- Some examples require specific toolchains. The Python/NumPy example runs anywhere.
- AVX and OpenMP examples produce timing outputs. CUDA example requires GPU & nvcc.
