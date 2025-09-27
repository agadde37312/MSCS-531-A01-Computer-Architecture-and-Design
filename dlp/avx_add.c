\
 // avx_add.c
 // Compile with: gcc -O3 -mavx -std=c11 avx_add.c -o avx_add
 #include <immintrin.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <time.h>

 double now() {
     struct timespec t;
     clock_gettime(CLOCK_MONOTONIC, &t);
     return t.tv_sec + t.tv_nsec * 1e-9;
 }

 int main(int argc, char** argv) {
     int N = 1000000;
     if (argc > 1) N = atoi(argv[1]);
     float *a = (float*) aligned_alloc(32, N * sizeof(float));
     float *b = (float*) aligned_alloc(32, N * sizeof(float));
     float *c = (float*) aligned_alloc(32, N * sizeof(float));
     for (int i=0;i<N;i++){ a[i]= (float)i; b[i]=(float)i; }

     double t0 = now();
     // scalar add
     for (int i=0;i<N;i++) c[i] = a[i] + b[i];
     double t1 = now();
     printf("scalar_time %d %f\n", N, t1-t0);

     // avx add (8 floats per 256-bit)
     t0 = now();
     int i;
     for (i=0; i+8 <= N; i+=8) {
         __m256 va = _mm256_load_ps(&a[i]);
         __m256 vb = _mm256_load_ps(&b[i]);
         __m256 vc = _mm256_add_ps(va, vb);
         _mm256_store_ps(&c[i], vc);
     }
     // tail
     for (; i<N; i++) c[i] = a[i] + b[i];
     t1 = now();
     printf("avx_time %d %f\n", N, t1-t0);

     // prevent optimizing out
     printf("c[0]=%f c[N-1]=%f\n", c[0], c[N-1]);
     free(a); free(b); free(c);
     return 0;
 }
