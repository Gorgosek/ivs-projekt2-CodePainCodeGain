import sys
import numpy as np

def read_and_compute_std():
    # Parse input from stdin
    input_data = sys.stdin.read()
    string_values = input_data.split()
    
    # Make an array of floating point numbers
    float_values = np.array(string_values, dtype=np.float64)
    
    # Calculate the standard deviation
    S = np.std(float_values)
    return S

if __name__ == "__main__":
    # Print the computed standard deviation
    print("Standard Deviation:", read_and_compute_std())
