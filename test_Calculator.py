import Calculator
import pytest

@pytest.mark.parametrize("x,y,z",[(2,6,5),(7,3,6),(0,9,0)])
def test_add(x,y,z):
    result=Calculator.add2no(x,y)
    assert result == z

@pytest.mark.parametrize("x,y,z",[(6,9,0),(3,8,2),(3,9,9)])
def test_sub(x,y,z):
    result=Calculator.sub2no(x,y)
    assert result == z

@pytest.mark.parametrize("x,y,z",[(3,2,2),(1,9,3)])
def test_mul(x,y,z):
    result=Calculator.mul2no(x,y)
    assert result == z

@pytest.mark.parametrize("x,y,z",[(0,0,1),(2,1,9)])
def test_div(x,y,z):
    result=Calculator.div2no(x,y)
    assert result == z