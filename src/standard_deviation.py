#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file standard_deviation.py
#
# @brief A standalone program that calculates standard deviation (sampling)
#
# @section description_standard_deviation Description
# - Reads input values from system stdin
# - Computes the sampling variant of standard deviation 
# - Uses functions from the CalculatorMathLib module, instead of using the native operators
#
# @section author_standard_deviation Author(s)
# xnezbea00
import sys # for stdin use
from calculatormathlib import CalculatorMathLib # Used for CalculatorMathLib() object


nums = []

def read_stdin():
    """! Reads input values from stdin into a list called nums.

    This function processes each line of stdin, splitting the line by any amount of whitespaces,
    attempting to convert each split value into a float, and appending floats to nums.

    @section details Details
    Assumes input is a number of a float value with . as its decimal separator.
    """
    for line in sys.stdin:
        # Get rid of whitespaces
        lineVals = line.strip().split()

        # Only consider correct float values from input
        for value in lineVals:
            floatVal = float(value)
            nums.append(floatVal)

# Object for mathlib functions
Math = CalculatorMathLib()

# Calculates the sum of all numbers in an array 
def sum(nums):
    """! Calculates the sum of all values in a list

    Uses the CalculatorMathLib add function to compute the sum to avoid floating point precision issues.

    @param nums List of numbers (floats) to sum.

    @return The sum of all numbers in the list.
    """
    res = 0
    for num in nums:
        res = Math.add(res, num)

    return res

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

    The function first calculates the mean of the numbers, then uses that mean to calculate the sum of squared differences.
    Finally, it divides that sum by (N-1) and takes the square root to find the standard deviation.

    @param nums List of numbers (floats).

    @return The standard deviation of the numbers.
    """
    sumOfNums = sum(nums)
    argsLen = len(nums)     # Accounts for 0eth element correctly

    # barX signifies the mean 
    barX = Math.div(sumOfNums, argsLen)


    # Final equation using s = sqrt(sum_of_squared_differences/argsLen-1)
    S = Math.sqrt(Math.div(sum_of_squared_differences(nums, barX), Math.sub(argsLen, 1)))
    return S


def main():
    """! Main function to execute the program's functionality.

    Reads values from stdin, calculates the standard deviation, and prints the result.
    Also handles the case of invalid input (less than 2 numbers).
    """
    # Fills up nums[] array with values
    read_stdin()
    # Formula expects at least 2 numbers
    if len(nums) <= 1:
        print("Invalid input")
        return

    # Calcualates the standard_deviation using the numbers from the nums array
    S = standard_deviation(nums)
    print(S)

if __name__ == "__main__":
    main()


