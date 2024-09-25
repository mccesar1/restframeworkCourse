"""
sample tests
"""
from django.test import SimpleTestCase
from app import cal 

class ClacTest(SimpleTestCase):
    """ Test the add function from the cal module """
    def test_add(self):
        """ Test that the addition of two numbers returns the correct total """
        res = cal.add(3, 2)
        self.assertEqual(res, 5)

    def test_subtract(self):
        """ Test that the subtraction of two numbers returns the correct total """
        res = cal.subtract(3, 2)
        self.assertEqual(res, 1)