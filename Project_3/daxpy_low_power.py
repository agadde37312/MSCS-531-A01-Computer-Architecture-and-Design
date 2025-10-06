# daxpy_low_power.py
import threading
import numpy as np

def daxpy(a, x, y, start, end):
    for i in range(start, end):
        y[i] = a*x[i] + y[i]

def main():
    N = 5000000
    a = 2.5
    x = np.random.rand(N)
    y = np.random.rand(N)

    num_threads = 4
    threads = []
    chunk = N // num_threads

    for i in range(num_threads):
        start = i * chunk
        end = N if i == num_threads-1 else (i+1)*chunk
        t = threading.Thread(target=daxpy, args=(a, x, y, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"DAXPY completed for {N} elements with {num_threads} threads.")

if __name__ == "__main__":
    main()
