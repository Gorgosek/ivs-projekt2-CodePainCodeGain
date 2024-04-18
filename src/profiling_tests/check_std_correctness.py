import sys
import statistics

nums = []
def compute_std(arr):
    # S = np.std(arr) - CALCULATES POPULATION
    S = statistics.stdev(arr)
    return S

def read_stdin():
    for line in sys.stdin:
        # Get rid of whitespaces
        lineVals = line.strip().split()

        # Only consider correct float values from input
        for value in lineVals:
            floatVal = float(value)
            nums.append(floatVal)


if __name__ == "__main__":
    # Print the computed standard deviation
    read_stdin()
    print(compute_std(nums))
