import pytest
from calc.ops import add, multiply

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1,2,3),
        (-5,5,0),
        (2.5,0.5,3.0),
        (0,0,0),
        (10,-3,7)
    ],
)
def test_add(a,b,expected):
    assert add(a,b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1,2,2),
        (-5,5,-25),
        (2.5,0.5,1.25),
        (10,-3,-30)
    ],
)
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected