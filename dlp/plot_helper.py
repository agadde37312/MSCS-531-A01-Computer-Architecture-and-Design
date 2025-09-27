# plot_helper.py
import pandas as pd
import matplotlib.pyplot as plt
import sys, os

def plot_csv(csvfile, xcol, ycol, out):
    df = pd.read_csv(csvfile)
    plt.figure(figsize=(6,4))
    plt.plot(df[xcol], df[ycol], marker='o')
    plt.xlabel(xcol); plt.ylabel(ycol)
    plt.grid(True); plt.tight_layout()
    plt.savefig(out)
    print('Saved', out)

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: plot_helper.py data.csv xcol ycol out.png')
        sys.exit(1)
    plot_csv(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
