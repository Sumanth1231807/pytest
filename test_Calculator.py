import Calculator
def test_add():
    x=2
    y=6
    result = Calculator.add2no(x,y)
    assert  result==x+y


def test_sub():
    x = 2
    y = 6
    result = Calculator.sub2no(x, y)
    assert result == x - y


def test_mul():
    x = 2
    y = 6
    result = Calculator.mul2no(x, y)
    assert result == x*y


def test_div():
    x = 2
    y = 6
    result = Calculator.div2no(x, y)
    assert result == x / y