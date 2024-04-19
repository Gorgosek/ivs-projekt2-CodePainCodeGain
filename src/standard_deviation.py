import cProfile
import pstats
from pstats import SortKey
import sys # for stdin use
import numpy as np
from calculatormathlib import CalculatorMathLib # Used for CalculatorMathLib() object


def read_stdin():
    input_data = sys.stdin.read()
    float_vals = np.array(input_data.split(), dtype=np.float64)
    return float_vals


# Object for mathlib functions
Math = CalculatorMathLib()

# Calculates the sum of all numbers in an array 
def sum(nums):
    res = 0
    for num in nums:
        res = Math.add(res, num)

    return res

# Sums the difference of (num - barNum)^2 for all numbers from the array nums
# barNum is supposed to be the mean
def sum_of_squared_differences(nums, barNum):
    res = 0
    for num in nums:
        powRes = Math.pow2(num - barNum)
        res = Math.add(res, powRes)
    return res


def standard_deviation(nums):
    sumOfNums = sum(nums)
    argsLen = len(nums)     # Accounts for 0eth element correctly

    # barX median also medX
    barX = Math.div(sumOfNums, argsLen)


    # Final equation using s = sqrt(sum_of_squared_differences/argsLen-1)
    S = Math.sqrt(Math.div(sum_of_squared_differences(nums, barX), Math.sub(argsLen, 1)))
    return S


def main():
    # Fills up nums[] array with values
    nums = read_stdin()

    # Calcualates the standard_deviation using the numbers from the nums array
    S = standard_deviation(nums)
    print(S)

if __name__ == "__main__":
    cProfile.run('main()', "profiling_stats")
    p = pstats.Stats("profiling_stats")
    p.strip_dirs().sort_stats(SortKey.TIME).print_stats()


