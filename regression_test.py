import pytest
from calculator import add ,subtract
def test_add_existing():
    assert add (1,2)==3

def test_subtract_existing():
    assert subtract(4,2)==2

def test_new_functinality():
    assert add(0,0)==0