#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(int argc, char **argv) {
    if (argc < 4) {
        printf("Usage: %s <N> <threads> <repeat>\\n", argv[0]);
        return 1;
    }
    long N = atol(argv[1]);
    int threads = atoi(argv[2]);
    int repeat = atoi(argv[3]);
    omp_set_num_threads(threads);

    double *x = (double*) aligned_alloc(64, sizeof(double)*N);
    double *y = (double*) aligned_alloc(64, sizeof(double)*N);
    if (!x || !y) {
        perror("aligned_alloc");
        return 1;
    }
    double a = 3.14159;
    for (long i = 0; i < N; ++i) { x[i] = 1.0*(i+1); y[i] = 2.0*(i+1); }

    double t0 = omp_get_wtime();
    for (int r = 0; r < repeat; ++r) {
        #pragma omp parallel for schedule(static)
        for (long i = 0; i < N; ++i) {
            y[i] = a * x[i] + y[i];
        }
    }
    double t1 = omp_get_wtime();

    double sum = 0.0;
    for (long i = 0; i < N; ++i) sum += y[i];

    printf("N=%ld threads=%d repeat=%d time=%.6f checksum=%e\\n", N, threads, repeat, t1 - t0, sum);

    free(x); free(y);
    return 0;
}
