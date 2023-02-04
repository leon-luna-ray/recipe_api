"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Sample test cases """

    def test_add_numbers(self):
        """ Test adding numbers together """
        res = calc.add(5, 5)

        self.assertEqual(res, 10)

    def test_subtract_numbers(self):
        """ Test subtracting numbers """
        res = calc.subtract(100, 99)
        self.assertEqual(res, 1)
