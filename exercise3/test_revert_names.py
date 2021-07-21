import unittest
from exercise3 import revert_names
from exercise3.invalid_sequence_of_names_exception import InvalidSequenceOfNamesException


class MyTestCase(unittest.TestCase):

    def test_reverse_string_valid_names(self):
        self.assertEqual(revert_names.reverse_string("John Doe"), "eoD nhoJ")

    def test_reverse_string_short_valid_names(self):
        self.assertEqual(revert_names.reverse_string("a b"), "b a")

    def test_reverse_string_long_valid_names(self):
        self.assertEqual(revert_names.reverse_string("Abcdefghijklmnopqrstuvxz Abcdefghijklmnopqrstuvxz"),
                         "zxvutsrqponmlkjihgfedcbA zxvutsrqponmlkjihgfedcbA")

    def test_reverse_string_invalid_number_of_names(self):
        with self.assertRaises(InvalidSequenceOfNamesException):
            revert_names.reverse_string("name name name")
            revert_names.reverse_string("name")
            revert_names.reverse_string("a b joao silva")

    def test_reverse_string_invalid_empty_name(self):
        with self.assertRaises(InvalidSequenceOfNamesException):
            revert_names.reverse_string(" ")
            revert_names.reverse_string("                        ")

    def test_reverse_string_invalid_name_limited_by_space(self):
        with self.assertRaises(InvalidSequenceOfNamesException):
            revert_names.reverse_string(" a b c")
            revert_names.reverse_string(" ac")
            revert_names.reverse_string(" a b ")
            revert_names.reverse_string("a c ")

    def test_reverse_string_invalid_names_with_numbers(self):
        with self.assertRaises(InvalidSequenceOfNamesException):
            revert_names.reverse_string("213457")
            revert_names.reverse_string("777 sdfff")
            revert_names.reverse_string("dffs 123")
            revert_names.reverse_string("213 457")

    def test_is_valid_sequence_of_words_valid_words(self):
        self.assertTrue(revert_names.is_valid_sequence_of_words("Maria Silva"))
        self.assertTrue(revert_names.is_valid_sequence_of_words("Tassio Zizo"))
        self.assertTrue(revert_names.is_valid_sequence_of_words("Wall St"))

    def test_is_valid_sequence_of_words_valid_words(self):
        self.assertFalse(revert_names.is_valid_sequence_of_words("Maria Silva Santos"))
        self.assertFalse(revert_names.is_valid_sequence_of_words("123 123"))
        self.assertFalse(revert_names.is_valid_sequence_of_words("!@# %*"))
