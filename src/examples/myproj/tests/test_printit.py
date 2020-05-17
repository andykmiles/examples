import pytest
import myproj.printit
def test_printit():
    value = myproj.printit.p("hello from test")
    assert value == 99
