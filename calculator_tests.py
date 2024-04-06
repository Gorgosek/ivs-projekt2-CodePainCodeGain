# calculator_tests.py
# Projekt IVS2
# Autor: Novotný Tadeáš, xnovott00
# Datum: 2024-04-06

import unittest

from src.%% import %%%%

# Tests of an addition (+)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_addition_positive_numbers(self):
        self.assertEqual(self.math.add(1, 3), 4)
        self.assertEqual(self.math.add(0, 0), 0)
        self.assertEqual(self.math.add(0, 7), 7)
        self.assertEqual(self.math.add(77, 34), 111)
    
    def test_addition_negative_numbers(self):
        self.assertEqual(self.math.add(-1, -1), -2)
        self.assertEqual(self.math.add(0, -7), -7)
        self.assertEqual(self.math.add(-11, 0), -11)
        self.assertEqual(self.math.add(-77, -34), -111)

    def test_addition_negative_positive_numbers(self):
        self.assertEqual(self.math.add(-5, 2), -3)
        self.assertEqual(self.math.add(1, -7), -6)
        self.assertEqual(self.math.add(11, -10), 1)
        self.assertEqual(self.math.add(-11, 11), 0)

    def test_addition_decimal_numbers(self):
        self.assertEqual(self.math.add(2.5, 7.5), 10)
        self.assertEqual(self.math.add(1.5, 7.25), 8.75)
        self.assertEqual(self.math.add(-1.5, 7.25), 5.75)
        self.assertEqual(self.math.add(-1.5, -7.25), -8.75)

# Tests of a subtraction (-)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.math.sub(1, 3), -2)
        self.assertEqual(self.math.sub(0, 0), 0)
        self.assertEqual(self.math.sub(0, 7), -7)
        self.assertEqual(self.math.sub(77, 34), 43)
    
    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.math.sub(-1, -1), 0)
        self.assertEqual(self.math.sub(0, -7), 7)
        self.assertEqual(self.math.sub(-11, 0), -11)
        self.assertEqual(self.math.sub(-77, -34), -43)

    def test_subtraction_negative_positive_numbers(self):
        self.assertEqual(self.math.sub(-5, 2), -7)
        self.assertEqual(self.math.sub(1, -7), 8)
        self.assertEqual(self.math.sub(11, -10), 21)
        self.assertEqual(self.math.sub(-11, 11), -22)

    def test_subtraction_decimal_numbers(self):
        self.assertEqual(self.math.sub(2.5, 7.5), -5)
        self.assertEqual(self.math.sub(1.5, 7.25), -5.75)
        self.assertEqual(self.math.sub(-1.5, 7.25), -8.75)
        self.assertEqual(self.math.sub(-1.5, -7.25), 5.75)

# Tests of a multiplication (*)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.math.multiply(1, 3), 3)
        self.assertEqual(self.math.multiply(0, 0), 0)
        self.assertEqual(self.math.multiply(7, 0), 0)
        self.assertEqual(self.math.multiply(77, 34), 2618)
    
    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.math.multiply(-1, -1), 1)
        self.assertEqual(self.math.multiply(0, -7), 0)
        self.assertEqual(self.math.multiply(-11, 0), 0)
        self.assertEqual(self.math.multiply(-77, -34), 2618)

    def test_multiplication_negative_positive_numbers(self):
        self.assertEqual(self.math.multiply(-5, 2), -10)
        self.assertEqual(self.math.multiply(1, -7), -7)
        self.assertEqual(self.math.multiply(11, -10), -110)
        self.assertEqual(self.math.multiply(-11, 11), -121)

    def test_multiplication_decimal_numbers(self):
        self.assertEqual(self.math.multiply(2.5, 7.5), 18.75)
        self.assertEqual(self.math.multiply(1.5, 7.25), 10.875)
        self.assertEqual(self.math.multiply(-1.5, 7.25), -10.875)
        self.assertEqual(self.math.multiply(-1.5, -7.25), 10.875)

# Tests of a division (/)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_division_positive_numbers(self):
        self.assertEqual(self.math.div(25, 5), 5)
        self.assertEqual(self.math.div(120, 60), 2)
        self.assertEqual(self.math.div(0, 7), 0)
        self.assertEqual(self.math.div(777, 777), 1)
    
    def test_division_negative_numbers(self):
        self.assertEqual(self.math.div(-1, -1), 1)
        self.assertEqual(self.math.div(0, -7), 0)
        self.assertEqual(self.math.div(-12, -6), 2)
        self.assertEqual(self.math.div(-102, -34), 3)

    def test_division_negative_positive_numbers(self):
        self.assertEqual(self.math.div(-10, 5), -2)
        self.assertEqual(self.math.div(21, -7), -3)
        self.assertEqual(self.math.div(50, -10), -5)
        self.assertEqual(self.math.div(-11, 11), -1)

    def test_division_decimal_numbers(self):
        self.assertEqual(self.math.div(7.5, 2.5), 3)
        self.assertEqual(self.math.div(9, 4), 2.25)
        self.assertEqual(self.math.div(-1.5, 0.5), -3)
        self.assertAlmostEqual(self.math.div(-100, -30), 3.3333, 4)


    # Test division by zero should raise a ValueError {cannot be done}
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.div(7, 0)
            self.math.div(-7, 0)

# Tests of the power function (^)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_power_positive_numbers(self):
        self.assertEqual(self.math.power(2, 3), 8)
        self.assertEqual(self.math.power(5, 2), 25)
        self.assertEqual(self.math.power(10, 0), 1) 

    def test_power_negative_numbers(self):
        self.assertEqual(self.math.power(-2, 3), -8)
        self.assertEqual(self.math.power(-5, 2), 25)

    # Test unexpected exponents
    def test_power_unexpected_exponents(self):
        with self.assertRaises(ValueError):
            self.math.power(200, 0)
        with self.assertRaises(ValueError):
            self.math.power(20, -1)
        with self.assertRaises(ValueError):
            self.math.power(2, -20)
        with self.assertRaises(ValueError):
            self.math.power(2, 2.25)
        with self.assertRaises(ValueError):
            self.math.power(5, -0.2)

# Tests of the root function (√)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_square_root_positive_numbers(self):
        self.assertEqual(self.math.root(25, 2), 5) 
        self.assertEqual(self.math.root(27, 3), 3)
        self.assertEqual(self.math.root(0, 2), 0)   

    def test_square_root_decimal_numbers(self):
        self.assertEqual(self.math.root(0.5, 0.5), 0.25)  
        self.assertAlmostEqual(self.math.root(125.55, 2.5), 6.9107, 4)  

    # Test square root of negative numbers should raise a ValueError
    def test_square_root_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.math.root(-25, 2)
        with self.assertRaises(ValueError):
            self.math.root(-10, 4)  
    
    # Test square root with negative exponent should raise a ValueError
    def test_square_root_negative_exponent(self):
        with self.assertRaises(ValueError):
            self.math.root(125, -2)
        with self.assertRaises(ValueError):
            self.math.root(1, -10) 
        with self.assertRaises(ValueError):
            self.math.root(4, -2)

# Tests of the factorial function (!)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_factorial_positive_numbers(self):
        # Factorial of 0 is 1 by definition
        self.assertEqual(self.math.factorial(0), 1)  
        self.assertEqual(self.math.factorial(1), 1)  
        self.assertEqual(self.math.factorial(5), 120)
        self.assertEqual(self.math.factorial(11), 39916800)

    # Test factorial of negative number, expecting a ValueError
    def test_factorial_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.math.factorial(-1)
        with self.assertRaises(ValueError):
            self.math.factorial(-7)

    # Test factorial of decimal number, expecting a ValueError
    def test_factorial_decimal_numbers(self):
        with self.assertRaises(ValueError):
            self.math.factorial(1.5)
        with self.assertRaises(ValueError):
            self.math.factorial(-2.5)

# Tests of the natural logarithm function (ln)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_ln_positive_numbers(self):
        # natural ln of 1 is 0
        self.assertAlmostEqual(self.math.ln(1), 0)  
        self.assertAlmostEqual(self.math.ln(10), 2.302585, 6)  
        self.assertAlmostEqual(self.math.ln(0.5), -0.693147, 6)
        self.assertAlmostEqual(self.math.ln(2), 0.693147, 6)

    def test_ln_invalid_input(self):
        # ln(0) is undefined, should raise ValueError
        with self.assertRaises(ValueError):
            self.math.ln(0)
        # ln of negative number is undefined, should raise ValueError
        with self.assertRaises(ValueError):
            self.math.ln(-1)

# Tests of the log function (log)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_log_positive_numbers(self):
        self.assertAlmostEqual(self.math.log(10, 10), 1)
        self.assertAlmostEqual(self.math.log(100, 10), 2)  
        self.assertAlmostEqual(self.math.log(1, 10), 0) 

    def test_log_invalid_input(self):
        # log base 10 of 0 is undefined, should raise ValueError
        with self.assertRaises(ValueError):
            self.math.log(0, 10) 
        # log of negative number is undefined, should raise ValueError    
        with self.assertRaises(ValueError):
            self.math.log(-1, 10)

# Tests of the absolute function (|x|)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_absolute_positive_numbers(self):
        self.assertEqual(self.math.abs(5), 5)
        self.assertEqual(self.math.abs(10), 10) 

    def test_absolute_negative_numbers(self):
        self.assertEqual(self.math.abs(-5), 5) 
        self.assertEqual(self.math.abs(-10), 10) 

    def test_absolute_decimal_numbers(self):
        self.assertAlmostEqual(self.math.abs(3.14), 3.14)  
        self.assertAlmostEqual(self.math.abs(-2.5), 2.5)  

    def test_absolute_zero(self):
        self.assertEqual(self.math.abs(0), 0) 

# Tests of the modulo function (%)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%%Lib()

    def test_modulo_positive_numbers(self):
        self.assertEqual(self.math.modulo(10, 3), 1) 
        self.assertEqual(self.math.modulo(20, 7), 6) 

    def test_modulo_negative_numbers(self):
        self.assertEqual(self.math.modulo(-10, 3), 2)  
        self.assertEqual(self.math.modulo(10, -3), -2)  

    def test_modulo_zero(self):
        self.assertEqual(self.math.modulo(0, 5), 0)
    
    # x % 0 is undefined, should raise ValueError
    def test_modulo_zero2(self):
        with self.assertRaises(ValueError):
            self.math.modulo(10, 0)

    def test_modulo_decimal_numbers(self):
        self.assertAlmostEqual(self.math.modulo(10.5, 3), 1.5)
        self.assertAlmostEqual(self.math.modulo(-10.5, 3), 0.5) 

# Tests the solve_expression function
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = %%%Lib()

    def test_solve_expression_addition(self):
        self.assertEqual(self.math.solve_expression("2+7"), 9)
        self.assertEqual(self.math.solve_expression("-5+12"), 7)
        self.assertEqual(self.math.solve_expression("2+-4"), -2)
        self.assertEqual(self.math.solve_expression("1.5+7"), 8.5)
        self.assertEqual(self.math.solve_expression("6.3+-3.2"), 3.1)

    def test_solve_expression_subtraction(self):
        self.assertEqual(self.math.solve_expression("9-5"), 4)
        self.assertEqual(self.math.solve_expression("-15-7"), -22)
        self.assertEqual(self.math.solve_expression("9--3"), 12)
        self.assertEqual(self.math.solve_expression("1.5-7"), -5.5)
        self.assertEqual(self.math.solve_expression("6.3--3.2"), 9.5)

    def test_solve_expression_multiplication(self):
        self.assertEqual(self.math.solve_expression("3*6"), 18)
        self.assertEqual(self.math.solve_expression("-8*15"), -120)
        self.assertEqual(self.math.solve_expression("3*-4"), -12)
        self.assertEqual(self.math.solve_expression("1.5*6"), 9)
        self.assertEqual(self.math.solve_expression("6.3*-3.2"), -20.16)

    def test_solve_expression_division(self):
        self.assertEqual(self.math.solve_expression("8/4"), 2)
        self.assertEqual(self.math.solve_expression("-15/3"), -5)
        self.assertEqual(self.math.solve_expression("3/-2"), -1.5)
        self.assertEqual(self.math.solve_expression("1.5/3"), 0.5)
        self.assertEqual(self.math.solve_expression("6.3/-3.2"), -1.96875)

        # Division by zero is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("-6/0")

    def test_solve_expression_power(self):
        self.assertEqual(self.math.solve_expression("2^4"), 16)
        self.assertEqual(self.math.solve_expression("-5^3"), -125)
        self.assertEqual(self.math.solve_expression("-2^6"), 64)
        self.assertEqual(self.math.solve_expression("1.5^3"), 3.375)

    def test_solve_expression_square_root(self):
        self.assertEqual(self.math.solve_expression("3√27"), 3)
        self.assertEqual(self.math.solve_expression("√25"), 5)
        self.assertEqual(self.math.solve_expression("3√64"), 4)
        self.assertEqual(self.math.solve_expression("5√100000"), 10)

        # Even root of negative number is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("4√-16")
        with self.assertRaises(ValueError):
            self.math.solve_expression("√-25")

    def test_solve_expression_factorial(self):
        self.assertEqual(self.math.solve_expression("0!"), 1)
        self.assertEqual(self.math.solve_expression("1!"), 1)
        self.assertEqual(self.math.solve_expression("2!"), 2)
        self.assertEqual(self.math.solve_expression("5!"), 120)

        # Factorials of negative nad decimal numbers are forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("0.15!")
        with self.assertRaises(ValueError):
            self.math.solve_expression("-13!")

    def test_solve_expression_ln(self):
        self.assertEqual(self.math.solve_expression("ln1"), 0)
        self.assertAlmostEqual(self.math.solve_expression("ln0.5"), -0.693147, 6)
        self.assertAlmostEqual(self.math.solve_expression("ln10"), 2.302585, 6)

        # Natural logarithm of negative number or zero is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("ln0")
        with self.assertRaises(ValueError):
            self.math.solve_expression("ln-12")

    def test_solve_expression_absolute(self):
        self.assertEqual(self.math.solve_expression("|5|"), 5)
        self.assertEqual(self.math.solve_expression("|-10|"), 10)
        self.assertEqual(self.math.solve_expression("||-10||"), 10)
        self.assertEqual(self.math.solve_expression("|||-10|||"), 10)
        self.assertEqual(self.math.solve_expression("||5-10||"), 5)

    def test_solve_expression_modulo(self):
        self.assertEqual(self.math.solve_expression("5%3"), 2)
        self.assertEqual(self.math.solve_expression("-10%5"), 0)
        self.assertEqual(self.math.solve_expression("7%2"), 1)
        self.assertEqual(self.math.solve_expression("15%-4"), -1)
        self.assertEqual(self.math.solve_expression("5%-3"), -1)

        # Modulo by zero is forbidden in math
        with self.assertRaises(ValueError):
            self.math.solve_expression("10%0")

    def test_solve_expression_multiple_operations(self):
        self.assertEqual(self.math.solve_expression("10+20/2*5"), 60)
        self.assertEqual(self.math.solve_expression("2!*5+1"), 11)
        self.assertEqual(self.math.solve_expression("10*4/4+2-3*2/2^1"), 7)

    # Double subtraction is not allowed
        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*4+1--1!")
    
    # Natural logarithm of zero is undefined
        with self.assertRaises(ValueError):
            self.math.solve_expression("2!*4+1-ln0")

if __name__ == '__main__':
    unittest.main()

