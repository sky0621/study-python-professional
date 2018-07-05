import unittest

class TestIt(unittest.TestCase):

    def setUpModule(self):
        """モジュール単位のテスト環境の準備"""

    def tearDownModule(self):
        """モジュール単位のテスト環境の後始末"""

    def setUp(self):
        """テスト環境の準備"""

    def tearDown(self):
        """テスト環境の後始末"""

    def test_it(self):
        """このメソッドが１つのテストケース"""

    def test_one(self):
        """これは別のテストケース"""

    def test_sample(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3)
