from testfixtures import compare
import unittest

def add(a, b):
    return a + b

class TestIt(unittest.TestCase):

    def test_add(self):
     result = add(2, 3)
     compare(result, 5)
