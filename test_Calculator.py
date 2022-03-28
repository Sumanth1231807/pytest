import Calculator

def test_add2no():
    x=10
    y=20
    result=Calculator.add2no(x,y)
    assert result == x+y

def test_sub2no():
    x=10
    y=2
    result= Calculator.sub2no(x,y)
    assert result == x-y

def test_mul2no():
    x=10
    y=2
    result= Calculator.mul2no(x,y)
    assert result == x*y

def test_div2no():
    x=10
    y=2
    result= Calculator.div2no(x,y)
    assert result == x/y