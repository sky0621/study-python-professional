import unittest
from unittest import mock

class TestMock(unittest.TestCase):

    def test_any(self):
        m = mock.Mock()
        m.something.return_value = 10
        self.assertEqual(m.something("this-is-dummy-arg"), 10)
        self.assertTrue(m.something.called)

    def test_side_effect(self):
        m = mock.Mock()
        m.something.side_effect = Exception('oops')
        try:
            m.something('this-is-dummy-arg')
            self.fail()
        except Exception:
            pass
