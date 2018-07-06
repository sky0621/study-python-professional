import datetime
from testfixtures import Replacer, test_date

def test_is_last_of_month():
    d = datetime.date(2011, 11, 30)
    assert is_last_of_month(d), "%s" % d

def test_is_last_of_month_now():
    with Replacer() as r:
        r.replace('util.datetime', test_date(2011, 11, 30))
        assert test_is_last_of_month_now()
