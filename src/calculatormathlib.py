#!/usr/bin/python
# -*- coding: utf-8 -*-

class CalculatorMathLib:

    #+
    @staticmethod
    def add(a, b):
        return a + b
    
    #-

    #*

    #/

    #^

    #2√
    @staticmethod
    def sqrt(a):
        if (a < 0):
            return ValueError('ValueError')
        else:
            return round(a**0.5, 10)
        
    #n√
    @staticmethod
    def root(a, n):
        if (n%2 == 0) and (a < 0):
            return ValueError('ValueError')
        else:
            return round(a**(1/n), 10)

    #!
    @staticmethod
    def factorial(a):
        if type(a) != int or a < 0:
            return ValueError('ValueError')
        if a == 0 or a == 1:
            return 1
        else:
            return a * CalculatorMathLib.factorial(a-1)
        
    #%
