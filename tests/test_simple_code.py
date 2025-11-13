import pytest 
from simple_code import add, subtract, multiply, divide

def test_add():
    assert add(5, 7) == 12
    assert add (-4, 4) == 0
    assert add (1.5,1.5) == 3.0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
    assert subtract(5.0, 2.5) == 2.5

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 10) == -20
    assert multiply(-3, -9) == 27

def test_divde():
    assert divide(100, 25) == 4
    assert divide(-9, 3) == -3
    assert divide(4.4, 2.0) ==  2.2
    
    with pytest.raises(ValueError):
        divide(2, 0) 
'''   
def test_power():
    assert power(2, 3) == 8
    assert power(-2, 2) == 4
''' 