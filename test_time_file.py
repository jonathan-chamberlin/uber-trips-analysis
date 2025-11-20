import pytest
from time_file import date_format
from time_file import hour_format


def test_date_format() -> None:
    assert date_format("9/3/2014") == "2014/09/03"
    assert date_format("9/15/2014") == "2014/09/15"
    assert date_format("10/3/2014") == "2014/10/03"
    assert date_format("10/20/2014") == "2014/10/20"

def test_hour_format() -> None:
    assert hour_format(0) == "00:00"
    assert hour_format(1) == "01:00"
    assert hour_format(2) == "02:00"
    assert hour_format(10) == "10:00"
    assert hour_format(15) == "15:00"
    assert hour_format(20) == "20:00"