#!/bin/bash
set -euo pipefail
echo "Running NumPy vector example..."
python3 numpy_vector.py
echo "Done. numpy_vector_plot.png and numpy_results.csv created."

# Build AVX example if compiler available
if command -v gcc >/dev/null 2>&1; then
  echo "Building AVX example..."
  gcc -O3 -mavx -std=c11 avx_add.c -o avx_add || true
  if [ -f avx_add ]; then
    echo "Running avx_add..."
    ./avx_add 1000000 | tee avx_output.txt || true
  fi
fi

# Build OpenMP example
if command -v gcc >/dev/null 2>&1; then
  echo "Building OpenMP example..."
  gcc -O2 -fopenmp openmp_reduce.c -o openmp_reduce || true
  if [ -f openmp_reduce ]; then
    echo "Running openmp_reduce..."
    ./openmp_reduce 50000000 | tee openmp_output.txt || true
  fi
fi

# Build CUDA example if nvcc exists
if command -v nvcc >/dev/null 2>&1; then
  echo "Building CUDA example..."
  nvcc -O3 cuda_matmul.cu -o cuda_matmul || true
  if [ -f cuda_matmul ]; then
    echo "Running cuda_matmul..."
    ./cuda_matmul 256 | tee cuda_output.txt || true
  fi
fi

echo "All done. Check outputs and plots."
