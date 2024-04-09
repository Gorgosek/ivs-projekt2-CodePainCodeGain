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

    #√

    #!
    def factorial(a):
        if type(a) != int or n < 0:
            return ValueError('ValueError')
        if a == 0 or a == 1:
            return 1
        else:
            return a * CalculatorMathLib.factorial(a-1)
    #%
