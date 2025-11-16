import pytest
from time_file import date_format

def test_date_format() -> None:
    assert date_format("9/3/2014") == "2014/09/03"
    assert date_format("9/15/2014") == "2014/09/15"
    assert date_format("10/3/2014") == "2014/10/03"
    assert date_format("10/20/2014") == "2014/10/20"