import unittest
from unittest.mock import patch
from webtest import TestApp

def setUpModule():
    _setup_db()

def tearDownModule():
    _teardown_db()

def _init_data():
    # ここでデータを作成

def _init_search_results():
    # ここで、モックの外部システム結果を作成

class TestWithMock(unittest.TestCase):

    def _getTarget(self):
        from app import myapp
        app = TestApp(myapp)
        return app

    @patch('othersite.search')
    def test_it(mock_search):
        """ テスト """

        # 前提条件
        mock_search.return_value = _init_search_results()
        _init_data()

        # テスト対象を準備
        app = self._getTarget()

        # テスト対象を実行
        res = app.get('/?search_word=abcd')

        # 結果確認
        assert "20" in res
        mock_account.deposit.assert_called_with(q="abcd")
