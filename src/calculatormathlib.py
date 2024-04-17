#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @file calculatormathlib.py
#
# @brief Math library for calculator
#
# @section description_calculatormathlib Description
# - Math library with all functions used by the calculator
#   (+, -, *, /, ^2, ^n, 2√, n√, !, %)
#
# @section author_calculatormathlib Author(s)
# xnovott00, xhajekp00


class CalculatorMathLib:
    """! Class with math functions.

    Class with all the math functions used by calculator.
    """

    # +
    @staticmethod
    def add(a, b):
        """! Function to compute a sum of two numbers.

        @param a First number to add.
        @param b Second number to add.

        @return Sum of the two numbers.
        """
        return a + b

    # -
    @staticmethod
    def sub(a, b):
        """! Function to compute a difference of two numbers.

        @param a First number to be subtracted from.
        @param b Second number to be subtracted.

        @return Difference between the two numbers.
        """
        return a - b

    # *
    @staticmethod
    def multiply(a, b):
        """! Function to compute a multiple of two numbers.

        @param a First number to be multiplied.
        @param b Second number to be multiplied.

        @return Multiple of the two numbers.
        """
        return a * b

    # /
    @staticmethod
    def div(a, b):
        """! Function to divide two numbers.

        @param a Dividend.
        @param b Divisor.

        @return Quotient.
        @exception Raises ValueError if 'b' is zero - can't divide by zero.
        """
        if b == 0:
            raise ValueError("MATH ERROR")
        return a / b

    # ^2
    @staticmethod
    def pow2(a):
        """! Function to compute a second power of a number.

        @param a Number to compute the second power of.

        @return Second power of the number.
        """
        return a * a

    # ^n
    @staticmethod
    def power(a, n):
        """! Function to compute a Nth power of a number.

        @param a Base number.
        @param n Exponent.

        @return Nth power of given number.
        """
        if (n < 0):
            raise ValueError("ERROR")
        if not (n % 1 == 0):
            raise ValueError("ERROR")
        return a**n

    # 2√
    @staticmethod
    def sqrt(a):
        """! Function to compute a square root of given number.

        @param a Number to compute the square root of.

        @return Square root of given number.
        @exception Raises ValueError if given number is negative.
        """
        if a < 0:
            raise ValueError("MATH ERROR")
        return a**0.5

    # n√
    @staticmethod
    def root(a, n):
        """! Function to compute a nth root of given number.

        @param a Number to compute the Nth root of.
        @param n Number representing Nth root.

        @return Nth root of given number.
        @exception Raises ValueError if 'n' is negative.
        @exception Raises ValueError if 'n' is even and 'a' is negative.
        """
        if n < 0:
            raise ValueError("MATH ERROR")
        if (n % 2 == 0) and (a < 0):
            raise ValueError("MATH ERROR")
        if (a < 0) and (n % 1 == 0):
            return -((-a) ** (1 / n))
        else:
            return (a) ** (1 / n)

    #!
    @staticmethod
    def factorial(a):
        """! Function to compute a factorial of given number.

        @param a Number to compute the factorial of.

        @return Returns factorial of given number.
        @exception Raises ValueError if given number isn't integer.
        @exception Raises ValueError if given number is negative.
        """
    
        if not (a % 1 == 0):
            raise ValueError("MATH ERROR")
        if a < 0:
            raise ValueError("MATH ERROR")
        if a == 0 or a == 1:
            return 1
        else:
            return a * CalculatorMathLib.factorial(a - 1)

    # %
    @staticmethod
    def modulo(a, b):
        """! Function to compute a remainder after dividing two numbers.

        @param a First number to be divided.
        @param b Second number to be divided by.

        @return Remainder after division of the two numbers.
        @exception Raises ValueError if the numbers aren't integers.
        @exception Raises ValueError if 'b' is zero - can't divide by zero.
        """
        if b == 0:
            raise ValueError("MATH ERROR")
        return a % b
