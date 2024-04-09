#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file calculatormathlib.py
#
# @brief Math library for calculator
#
# @section description_calculatormathlib Description
# - Math library with all functions used by the calculator
#   (+, -, *, /, ^, 2√, n√, %)
#
# @section todo_calculatormathlib TODO
# Add functions - sub, mul, div, pow, mod
#
# @section author_calculatormathlib Author(s)
# xnovott00, xhajekp00

class CalculatorMathLib:
    """! Class with math functions.

    Class with all the math functions used by calculator.
    """

    #+
    @staticmethod
    def add(a, b):
        """! Function to compute a sum of two numbers.

        @param a First number to add.
        @param b Second number to add.

        @return Sum of the two numbers.
        """
        return a + b
    
    #-

    #*

    #/

    #^

    #2√
    @staticmethod
    def sqrt(a):
        """! Function to compute a square root of given number.

        @param a Number to compute the square root of.

        @return Square root of given number.
        @return ValueError if given number is negative.
        """
        if (a < 0):
            return ValueError('ValueError')
        else:
            return round(a**0.5, 10)
        
    #n√
    @staticmethod
    def root(a, n):
        """! Function to compute a nth root of given number.

        @param a Number to compute the Nth root of.
        @param n Number representing Nth root.

        @return Nth root of given number.
        @return Returns ValueError if "n" is even and "a" is negative.
        """
        if (n%2 == 0) and (a < 0):
            return ValueError('ValueError')
        else:
            return round(a**(1/n), 10)

    #!
    @staticmethod
    def factorial(a):
        """! Function to compute a factorial of given number.

        @param a Number to compute the factorial of.

        @return Returns factorial of given number.
        @return ValueError if given number isn't integer or if it is negative.
        """
        if type(a) != int or a < 0:
            return ValueError('ValueError')
        if a == 0 or a == 1:
            return 1
        else:
            return a * CalculatorMathLib.factorial(a-1)
        
    #%
