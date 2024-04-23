##
# @file check_std_correctness.py
#
# @brief Numpy optimized version, outputs precise result of statistics.stdev function. 
#
# @section description_np_standard_deviation Description
# - Reads input values from system stdin
# - Computes the sampling variant of standard deviation 
# - Uses cProfile for profiling output
#
# @section author_standard_deviation Author(s)
# xnezbea00

import sys
import statistics
import numpy as np
import cProfile
import pstats
from pstats import SortKey

def compute_std(arr):
    """! Compute the sampling standard deviation of an array of numbers.

    This function uses the statistics.stdev function to calculate the sampling standard deviation,
    which is the square root of the estimated variance of the population based on sample data.

    @param arr An array of numbers (float64) for which the standard deviation is calculated.

    @return Result of standard deviation using statistics.stdev function
    """

    S = statistics.stdev(arr)
    return S

def read_stdin():
    """! Read and convert input from standard input into a numpy array of float64.

    This function reads a single input from standard input, splits the input string into components,
    converts each to a float, and returns a numpy array of these floats.

    @return A numpy array of float64 numbers read from standard input.
    """
    input_data = sys.stdin.read()
    float_vals = np.array(input_data.split(), dtype=np.float64)
    return float_vals

def main():
    """! Main function used when calling profiler to measure performance.

    Reads values from stdin, computes the standard deviation, and prints the result.
    Additionally, this function is profiled for performance analysis.

    """
    # Print the computed standard deviation
    nums = read_stdin()
    print(compute_std(nums))

if __name__ == "__main__":
    cProfile.run('main()', "profiling_stats")
    p = pstats.Stats("profiling_stats")
    p.strip_dirs().sort_stats('time').print_stats()
