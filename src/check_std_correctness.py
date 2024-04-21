import sys
import statistics
import numpy as np
import cProfile
import pstats
from pstats import SortKey

def compute_std(arr):
    # S = np.std(arr) - CALCULATES POPULATION
    S = statistics.stdev(arr)
    return S

def read_stdin():
    input_data = sys.stdin.read()
    float_vals = np.array(input_data.split(), dtype=np.float64)
    return float_vals

def main():
    # Print the computed standard deviation
    nums = read_stdin()
    print(compute_std(nums))

if __name__ == "__main__":
    cProfile.run('main()', "profiling_stats")
    p = pstats.Stats("profiling_stats")
    p.strip_dirs().sort_stats('time').print_stats()
