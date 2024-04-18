import random

def generate_floats(num_floats, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(num_floats)]

# Number of floats to generate
num_floats = 1_000
# Interval bounds
lower_bound = -1_000_000
upper_bound = 1_000_000

if __name__ == "__main__":
    floats = generate_floats(num_floats, lower_bound, upper_bound)
    # Num of decimals_places = 7
    decimals_places = 7
    rounded_floats = [round(fl, decimals_places) for fl in floats]
    print(" ".join(map(str, rounded_floats)))
