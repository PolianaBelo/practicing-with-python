import unittest
from exercise4 import triangle_types


class MyTestCase(unittest.TestCase):
    def test_define_triangle_isosceles(self):
        self.assertEqual(triangle_types.define_triangle_type([2, 2, 3]), "Isosceles")
        self.assertEqual(triangle_types.define_triangle_type([8, 8, 20]), "Isosceles")
        self.assertEqual(triangle_types.define_triangle_type([100, 8, 100]), "Isosceles")
        self.assertEqual(triangle_types.define_triangle_type([2000, 10000, 10000]), "Isosceles")

    def test_define_triangle_equilateral(self):
        self.assertEqual(triangle_types.define_triangle_type([1, 1, 1]), "Equilateral")
        self.assertEqual(triangle_types.define_triangle_type([55, 55, 55]), "Equilateral")
        self.assertEqual(triangle_types.define_triangle_type([900, 900, 900]), "Equilateral")
        self.assertEqual(triangle_types.define_triangle_type([44444, 44444, 44444]), "Equilateral")

    def test_define_triangle_scalene(self):
        self.assertEqual(triangle_types.define_triangle_type([1, 2, 3]), "Scalene")
        self.assertEqual(triangle_types.define_triangle_type([50, 5, 5000]), "Scalene")
        self.assertEqual(triangle_types.define_triangle_type([10035, 950, 207]), "Scalene")
        self.assertEqual(triangle_types.define_triangle_type([44, 708, 306]), "Scalene")

    def test_contains_zero_or_negative_numbers_with_negative_and_zero_numbers(self):
        self.assertTrue(triangle_types.contains_zero_or_negative_numbers([0, -2000, -4, -80, -33, 0]))
        self.assertTrue(triangle_types.contains_zero_or_negative_numbers([0, 0, 0, 0, 0]))
        self.assertTrue(triangle_types.contains_zero_or_negative_numbers([0]))
        self.assertTrue(triangle_types.contains_zero_or_negative_numbers([-1]))

    def test_contains_zero_or_negative_numbers_with_positive_numbers(self):
        self.assertFalse(triangle_types.contains_zero_or_negative_numbers([7, 2000, 4, 80, 33, 9999999]))
        self.assertFalse(triangle_types.contains_zero_or_negative_numbers([1.1, 9]))
        self.assertFalse(triangle_types.contains_zero_or_negative_numbers([100000]))
        self.assertFalse(triangle_types.contains_zero_or_negative_numbers([1]))

    def test_is_valid_triangle_with_valid_values(self):
        self.assertTrue(triangle_types.is_valid_triangle([1, 2, 3]))
        self.assertTrue(triangle_types.is_valid_triangle([7, 10, 5]))

    def test_is_valid_triangle_with_invalid_values(self):
        self.assertFalse(triangle_types.is_valid_triangle([1, 1, 3000]))
        self.assertFalse(triangle_types.is_valid_triangle([1, 10, 12]))

    def test_check_input_validity_invalid_input(self):
        self.assertFalse(triangle_types.is_valid_triangle([-1, 1, 3000]))
        self.assertFalse(triangle_types.is_valid_triangle([1, 10, 12]))

    def test_check_input_validity_valid_input(self):
        self.assertTrue(triangle_types.is_valid_triangle([4, 4, 4]))
        self.assertTrue(triangle_types.is_valid_triangle([10, 10, 12]))
