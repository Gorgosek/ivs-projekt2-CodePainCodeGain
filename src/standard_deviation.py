import sys # for stdin use
from calculatormathlib import CalculatorMathLib # Used for CalculatorMathLib() object


nums = []
def read_stdin():
    for line in sys.stdin:
        # Get rid of whitespaces
        lineVals = line.strip().split()

        # Only consider correct float values from input
        for value in lineVals:
            floatVal = float(value)
            nums.append(floatVal)

# Object for mathlib functions
Math = CalculatorMathLib()

def sum(nums):
    res = 0
    for num in nums:
        res += num

    return res

def sum_of_squared_differences(nums, barNum):
    res = 0
    for num in nums:
        res += Math.pow2(num - barNum)
    return res


def standard_deviation():
    sumOfNums = sum(nums)
    argsLen = len(nums)     # Accounts for 0eth element

    # barX median also medX
    barX = Math.div(sumOfNums, argsLen)


    S = Math.sqrt(Math.div(sum_of_squared_differences(nums, barX), argsLen-1))
    return S


if __name__ == "__main__":
    # Fills up nums[] array with values
    read_stdin()
    S = standard_deviation()
    print(S)


