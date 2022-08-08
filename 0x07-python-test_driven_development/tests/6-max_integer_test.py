#!/usr/bin/python3
"""6-max_integer test unit
"""
import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Defintion of of test unit for the max_integer function
    Functions:
        test_bad_input()
        test_output()
    """

    def setUp(self):
        """sets data for tests
        """
        self.not_list = ["", "fkjk", (12, 34, 11, 45, 132, 123), 0, 0.0]
        self.list_of_str = ["&'fhejk", "dsfhoihe", "fhfoijef", "nenfek"]
        self.list_of_float = [3.4, 234.0, -223.234, 0.0]
        self.list_of_int = [3, 4, 234, 0, -223, 234]

    def test_bad_input(self):
        """test result if bad input
        """
        with self.assertRaises(TypeError):
            for i in range(0, len(self.not_list)):
                max_integer(self.not_list[i])

    def test_output(self):
        """test result if input is accepted
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(self.list_of_int), 234)
        self.assertRaises(TypeError, max_integer(self.list_of_str))
        self.assertRaises(TypeError, max_integer(self.list_of_float))
