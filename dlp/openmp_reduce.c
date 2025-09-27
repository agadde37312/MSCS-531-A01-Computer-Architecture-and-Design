 // openmp_reduce.c
 // Compile with: gcc -O2 -fopenmp openmp_reduce.c -o openmp_reduce
 #include <stdio.h>
 #include <stdlib.h>
 #include <omp.h>
 #include <time.h>

 double now() {
     struct timespec t;
     clock_gettime(CLOCK_MONOTONIC, &t);
     return t.tv_sec + t.tv_nsec * 1e-9;
 }

 int main(int argc, char** argv) {
     int N = 100000000;
     if (argc > 1) N = atoi(argv[1]);
     double sum = 0.0;
     double t0 = now();
 #pragma omp parallel for reduction(+:sum)
     for (int i=0;i<N;i++) sum += (double)i * 0.5;
     double t1 = now();
     printf("openmp_time %d %f sum=%f
", N, t1-t0, sum);
     return 0;
 }
