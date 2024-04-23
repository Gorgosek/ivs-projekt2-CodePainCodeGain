#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file generate_nums.py
#
# @brief Generator for a specfied amount of random floating point numbers
#
# @section description Description
# - Implicitly generates 1000
# - First passed argument determines the amount of numbers to generate 
# - Can be tweaked by internally changing the values of:
#   - Interval bounds (lower_bound, upper_bound) 
#   - decimals_places
#
# @section author Author(s)
# xnezbea00

import random
import sys

def generate_floats(num_floats, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(num_floats)]

# Number of floats to generate
num_floats = 1_000
# Interval bounds
lower_bound = -1_000_000_000
upper_bound = 1_000_000_000

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_floats = int(sys.argv[1])
    floats = generate_floats(num_floats, lower_bound, upper_bound)
    # Num of decimals_places = 7
    decimals_places = 10
    rounded_floats = [round(fl, decimals_places) for fl in floats]
    print(" ".join(map(str, rounded_floats)))
