# calculator_tests.py
# Projekt IVS2
# Autor: Novotný Tadeáš, xnovott00
# Datum: 2024-04-06

import unittest

from src.calculatormathlib import CalculatorMathLib

# Tests of an addition (+)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = CalculatorMathLib()

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
        self.math = CalculatorMathLib()

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
        self.math = CalculatorMathLib()

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
        self.math = CalculatorMathLib()

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

# Tests of the pow2 function (^2)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = CalculatorMathLib()

    def test_power_positive_numbers(self):
        self.assertEqual(self.math.pow2(1), 1)
        self.assertEqual(self.math.pow2(5), 25) 
        self.assertEqual(self.math.pow2(0), 0)

    def test_power_negative_numbers(self):
        self.assertEqual(self.math.pow2(-2), 4)
        self.assertEqual(self.math.pow2(-7), 49)


# Tests of the power function (^)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = CalculatorMathLib()

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


# Tests of the sqrt function (2√)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = CalculatorMathLib()

    def test_square_root_positive_numbers(self):
        self.assertEqual(self.math.root(25), 5) 
        self.assertEqual(self.math.root(4), 2)
        self.assertEqual(self.math.root(0), 0)    

    # Test square root of negative numbers should raise a ValueError
    def test_square_root_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.math.root(-25)
        with self.assertRaises(ValueError):
            self.math.root(-10)  

# Tests of the root function (√)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = CalculatorMathLib()

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
        self.math = CalculatorMathLib()

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

# Tests of the modulo function (%)
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.math = CalculatorMathLib()

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

# Additional tests, if needed
