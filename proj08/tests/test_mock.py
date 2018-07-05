import unittest
from unittest import mock

class TestMock(unittest.TestCase):

    def test_any(self):
        m = mock.Mock()
        m.something.return_value = 10
        self.assertEqual(m.something("this-is-dummy-arg"), 10)
