import pytest

def div(x,y):
    if y == 0:
        raise ValueError
    return x / y

def test_normal():
    result = div(6,2)
    assert result == 3

def test_zero():
    with pytest.raises(ValueError):
        div(1,0)