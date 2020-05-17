import pytest
from q3 import q3

def test_example_1():
    assert q3([6, 2]) == 12

def test_start_from_right_end():
    assert q3([6, 6]) == 8

def test_start_from_left_end():
    assert q3([9, 1]) == 20

def test_large_n():
    assert q3([1000000, 500000]) == 250000250710

def test_large_a1():
    with pytest.raises(ValueError):
        q3([5000, 10000])

def test_invalid_argument():
    with pytest.raises(TypeError):
        q3([5000, 'k'])
    with pytest.raises(ValueError):
        q3([5000])