import sys # for argv use
from calculatormathlib import CalculatorMathLib

nums = []

Math = CalculatorMathLib()

for arg in sys.argv[1:]:
    nums.append(float(arg))

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
    S = standard_deviation()
    print(S)


