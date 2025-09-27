# numpy_vector.py
# Vector vs scalar addition timing comparison and plotting
import numpy as np
import time
import csv
import matplotlib.pyplot as plt
import sys

def scalar_add(n):
    a = list(range(n))
    b = list(range(n))
    t0 = time.time()
    c = [a[i] + b[i] for i in range(n)]
    t1 = time.time()
    return t1 - t0

def vector_add(n):
    a = np.arange(n, dtype=np.float32)
    b = np.arange(n, dtype=np.float32)
    t0 = time.time()
    c = a + b
    t1 = time.time()
    return t1 - t0

def run_and_save(sizes, out_csv='numpy_results.csv'):
    rows = []
    for n in sizes:
        print(f'Running n={n} (scalar)')
        t_scalar = scalar_add(n)
        print(f' Running n={n} (vector)')
        t_vector = vector_add(n)
        rows.append((n, t_scalar, t_vector))
        print(f' n={n}: scalar={t_scalar:.6f}s vector={t_vector:.6f}s')
    with open(out_csv,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['n','scalar_s','vector_s'])
        w.writerows(rows)
    return out_csv

def plot(csvfile):
    import pandas as pd
    df = pd.read_csv(csvfile)
    plt.figure(figsize=(6,4))
    plt.plot(df['n'], df['scalar_s'], label='Scalar (Python list)')
    plt.plot(df['n'], df['vector_s'], label='Vector (NumPy)')
    plt.xlabel('Array length (n)')
    plt.ylabel('Time (s)')
    plt.title('Scalar vs Vector Addition')
    plt.legend()
    plt.grid(True)
    out='numpy_vector_plot.png'
    plt.savefig(out)
    print('Saved', out)

if __name__ == '__main__':
    sizes = [10000, 100000, 1000000, 5000000]
    if len(sys.argv) > 1:
        sizes = [int(x) for x in sys.argv[1].split(',')]
    csvfile = run_and_save(sizes)
    plot(csvfile)
