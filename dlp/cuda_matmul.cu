\
 // cuda_matmul.cu
 // Compile with: nvcc -O3 cuda_matmul.cu -o cuda_matmul
 #include <cuda.h>
 #include <stdio.h>
 #include <stdlib.h>

 __global__ void matmul_kernel(float* A, float* B, float* C, int N) {
     int row = blockIdx.y * blockDim.y + threadIdx.y;
     int col = blockIdx.x * blockDim.x + threadIdx.x;
     if (row < N && col < N) {
         float sum = 0.0f;
         for (int k=0;k<N;k++) sum += A[row*N + k] * B[k*N + col];
         C[row*N + col] = sum;
     }
 }

 int main(int argc, char** argv) {
     int N = 256;
     if (argc > 1) N = atoi(argv[1]);
     size_t bytes = N * N * sizeof(float);
     float *h_A = (float*) malloc(bytes);
     float *h_B = (float*) malloc(bytes);
     float *h_C = (float*) malloc(bytes);
     for (int i=0;i<N*N;i++) { h_A[i]=1.0f; h_B[i]=1.0f; }

     float *d_A, *d_B, *d_C;
     cudaMalloc(&d_A, bytes); cudaMalloc(&d_B, bytes); cudaMalloc(&d_C, bytes);
     cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);
     cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice);

     dim3 block(16,16); dim3 grid((N+15)/16, (N+15)/16);
     matmul_kernel<<<grid, block>>>(d_A, d_B, d_C, N);
     cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost);

     printf("C[0]=%f C[N*N-1]=%f\n", h_C[0], h_C[N*N-1]);
     cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
     free(h_A); free(h_B); free(h_C);
     return 0;
 }
