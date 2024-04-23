##
# @file np_standard_deviation.py
#
# @brief Numpy optimized calculation of standard deviation, profiles its output
#
# @section description_np_standard_deviation Description
# - Reads input values from system stdin
# - Computes the sampling variant of standard deviation 
# - Uses functions from the CalculatorMathLib module, instead of using native operators
#
# @section author_standard_deviation Author(s)
# xnezbea00

import cProfile
import pstats
from pstats import SortKey
import sys # for stdin use
import numpy as np
from calculatormathlib import CalculatorMathLib # Used for CalculatorMathLib() object


def read_stdin():
    """! Read and convert input from standard input into a numpy array of float64.

    This function reads a single input from standard input, splits the input string into components,
    converts each to a float, and returns a numpy array of these floats.

    @return A numpy array of float64 numbers read from standard input.
    """
    input_data = sys.stdin.read()
    float_vals = np.array(input_data.split(), dtype=np.float64)
    return float_vals


# Object for mathlib functions
Math = CalculatorMathLib()

# Sums the difference of (num - barNum)^2 for all numbers from the array nums
# barNum is supposed to be the mean
def sum_of_squared_differences(nums, barNum):
    """! Calculates the sum of the squared differences of every number from the mean.

    For each number in the list, computes the square of the difference between that number and the mean,
    then sums up all those squared values.

    @param nums List of numbers (floats).
    @param barNum The mean of the numbers from the list.

    @return Sum of the squared differences from the mean.
    """
    res = 0
    for num in nums:
        powRes = Math.pow2(num - barNum)
        res = Math.add(res, powRes)
    return res


def standard_deviation(nums):
    """! Computes the standard deviation of a list of numbers.

    Calculates the sampling version of standard deviation. Same as standard_deviation.
    Uses numpy.sum for optimization.

    @param nums List of numbers (float64).

    @return The standard deviation of the numbers.
    """
    sumOfNums = np.sum(nums)
    argsLen = len(nums)     # Accounts for 0eth element correctly

    # barX median also medX
    barX = Math.div(sumOfNums, argsLen)

    # Final equation using s = sqrt(sum_of_squared_differences/argsLen-1)
    S = Math.sqrt(Math.div(sum_of_squared_differences(nums, barX), Math.sub(argsLen, 1)))
    return S


def main():
    """! Main function used when calling profiler to measure performance.

    Reads values from stdin, calculates the optimized version of standard deviation, and prints the profiled result.
    Also handles the case of invalid input (less than 2 numbers). 
    """
    # Fills up nums[] array with values
    nums = read_stdin()
    if len(nums) <= 1:
        print("Invalid input")
        return

    # Calcualates the standard_deviation using the numbers from the nums array
    S = standard_deviation(nums)
    print(S)

if __name__ == "__main__":
    cProfile.run('main()', "profiling_stats")
    p = pstats.Stats("profiling_stats")
    p.strip_dirs().sort_stats('time').print_stats()


