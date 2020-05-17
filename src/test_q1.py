import pytest
from q1 import q1

def test_example_1():
    assert q1([0, 1, 2]) == 3

def test_example_2():
    assert q1([0, 1, 99]) == 0

def test_all_zero():
    assert q1([0, 0, 0]) == 512

def test_not_exist():
    assert q1([0, 0, 1000]) == 0

def test_invalid_args_length():
    with pytest.raises(ValueError):
        q1([0, 0])

def test_invalid_args_type():
    with pytest.raises(ValueError):
        q1([0, 0, 'x'])
