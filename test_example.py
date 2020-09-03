import pytest
from calc import CalcDistance, IsPrime

@pytest.mark.parametrize("input_ax, input_ay, input_bx, input_by, expected",[
    (1,4,4,0,5),
    (23,10,18,22,13),
    (0,0,24,-7,25),
    (0,0,0,0,0)
])
def test_CalcDistance(input_ax, input_ay, input_bx, input_by, expected):
    assert CalcDistance(input_ax,input_ay,input_bx,input_by) == expected


@pytest.mark.parametrize("input_x, expected",[
    (1,False),
    (2,True),
    (3,True),
    (4,False),
    (5,True),
    (6,False),
    (7,True),
    (8,False),
    (9,False),
    (10,False),
    (11,True),
    (12,False),
    (13,True),
    (14,False),
])
def test_IsPrime(input_x, expected):
   assert IsPrime(input_x) is expected

