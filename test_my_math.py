# to test my_math functions
import sys
import unittest
import pytest

from my_math import MyMath


class TestMyMath(unittest.TestCase):
    """ A sample class for testing of basic math functions """
    

    def setUp(self):
        """ Executed before every test case """
        self.my_math = MyMath()

    def tearDown(self):
        """ Executed after every test case """
        del self.my_math

    def test_addition_success(self):
        """ Test function to check addition of two numbers """
        expected_results = 4
        assert self.my_math.addition(2, 2) == expected_results
        self.assertEqual(self.my_math.addition(2, 2), expected_results)
        self.assertTrue(self.my_math.addition(2, 2) == expected_results)
        self.assertFalse(self.my_math.addition(2, 2) == 3)

    def test_addition_success_big_numbers(self):    
        """ Test function to check addition of two large numbers """
        expected_results_big = 4e9
        assert self.my_math.addition(2e9, 2e9) == expected_results_big
        self.assertEqual(self.my_math.addition(2e9, 2e9), expected_results_big)
        self.assertTrue(self.my_math.addition(2e9, 2e9) == expected_results_big)
        self.assertFalse(self.my_math.addition(2e9, 2e9) == 3e9)

    def test_addition_success_small_numbers(self):     
        """ Test function to check addition of two small numbers """
        expected_results_small = 4e-9
        assert self.my_math.addition(2e-9, 2e-9) == expected_results_small
        self.assertEqual(self.my_math.addition(2e-9, 2e-9), expected_results_small)
        self.assertTrue(self.my_math.addition(2e-9, 2e-9) == expected_results_small)
        self.assertFalse(self.my_math.addition(2e-9, 2e-9) == 3e-9)

    def test_addition_success_equal_to_zero(self):
        """ Test function to check if the sum of two numbers is zero """
        self.assertTrue(self.my_math.addition(2e-9, -2e-9) == 0)
        self.assertFalse(self.my_math.addition(2e-9, 2e-9) == 0)

    def test_addition_success_not_almost_equal_to_zero(self):
        """ Test function to check if the sum of two numbers is not or is almost zero """
        self.assertNotEqual(self.my_math.addition(2e-9, 2e-9), 0)
        self.assertAlmostEqual(self.my_math.addition(2e-9, 2e-9), 0)
        self.assertIsNot(self.my_math.addition(2e-9, 2e-9), 0)

    def test_addition_success_odd_result(self):
        """ Test function to check if the sum of two numbers is odd number """
        self.assertEqual(self.my_math.addition(2, 1) % 2, 1)

    def test_addition_success_even_result(self):
        """ Test function to check if the sum of two numbers is even number """
        self.assertEqual(self.my_math.addition(2, 2) % 2, 0)

    def test_addition_success_positive_result(self):
        """ Test function to check addition of two small numbers is positive """
        self.assertGreater(self.my_math.addition(2, 2), 0)
        self.assertGreater(self.my_math.addition(2e9, 2e9), 0)
        self.assertGreater(self.my_math.addition(2e-9, 2e-9), 0)

    def test_addition_success_negative_result(self):
        """ Test function to check addition of two small numbers is negative """
        self.assertLess(self.my_math.addition(2, -3), 0)
        self.assertLess(self.my_math.addition(2e9, -3e9), 0)
        self.assertLess(self.my_math.addition(2e-9, -3e-9), 0)

    def test_addition_type_error(self):
        """ Test function to check addition of two numbers with type mismatch """
        with self.assertRaises(TypeError):
            self.my_math.addition(2, '2')
    
    def test_addition_type_error_pytest(self):
        """ Test function to check addition of two numbers with type mismatch (pytest way) """
        with pytest.raises(TypeError):
            self.my_math.addition(2, '2')

    def test_subtraction_success(self):
        """ Test function to check subtraction of two numbers """
        expected_results = 1
        assert self.my_math.subtraction(3, 2) == expected_results
        self.assertEqual(self.my_math.subtraction(3, 2), expected_results)
        self.assertTrue(self.my_math.subtraction(3, 2) == expected_results)
        self.assertFalse(self.my_math.subtraction(3, 2) == 0)

    def test_subtraction_type_error(self):
        """ Test function to check subtraction of two numbers with type mismatch """
        with self.assertRaises(TypeError):
            self.my_math.subtraction(3, '2')

    def test_subtraction_type_error_pytest(self):
        """ Test function to check subtraction of two numbers with type mismatch (pytest way) """
        with pytest.raises(TypeError):
            self.my_math.subtraction(3, '2')

    def test_multiplication_success(self):
        """ Test function to check multiplication of two numbers """
        expected_results = 8
        assert self.my_math.multiplication(2, 4) == expected_results
        self.assertEqual(self.my_math.multiplication(2, 4), expected_results)
        self.assertTrue(self.my_math.multiplication(2, 4) == expected_results)
        self.assertFalse(self.my_math.multiplication(2, 4) == 6)

    def test_multiplication_type_error(self):
        """ Test function to check multiplication of two numbers with type mismatch """
        with self.assertRaises(TypeError):
            self.my_math.multiplication(2.0, '4')

    def test_multiplication_type_error_pytest(self):
        """ Test function to check multiplication of two numbers with type mismatch (pytest way) """
        with pytest.raises(TypeError):
            self.my_math.multiplication(2.0, '4')

    def test_division_success(self):
        """ Test function to check division of two numbers """
        expected_results = 2.5
        assert self.my_math.division(5, 2) == expected_results
        self.assertEqual(self.my_math.division(5, 2), expected_results)
        self.assertTrue(self.my_math.division(5, 2) == expected_results)
        self.assertFalse(self.my_math.division(5, 2) == 3)

    def test_division_type_error(self):
        """ Test function to check division of two numbers with type mismatch """
        with self.assertRaises(TypeError):
            self.my_math.division(5, '2')

    def test_division_type_error_pytest(self):
        """ Test function to check division of two numbers with type mismatch (pytest way) """
        with pytest.raises(TypeError):
            self.my_math.division(5, '2')

    def test_zero_division_error(self):
        """ Test function to check division by zero """
        with self.assertRaises(ZeroDivisionError):
            self.my_math.division(5, 0)

    def test_zero_division_error_pytest(self):
        """ Test function to check division by zero (pytest way) """
        with pytest.raises(ZeroDivisionError):
            self.my_math.division(5, 0)

if __name__ == '__main__':
    unittest.main(testRunner = unittest.TextTestRunner(verbosity = 5, stream = sys.stdout))
