from q2 import q2
import pytest

def test_example_1():
    assert q2([5, 2, 3]) == 'a:1,b:0,c:1'

def test_large_k():
    with pytest.raises(ValueError):
        q2([100, 1, 3000])

def test_large_q():
    with pytest.raises(ValueError):
        q2([5, 2, 300])

def test_invalid_argument():
    with pytest.raises(TypeError):
        q2([5, 2, 'k'])
    with pytest.raises(ValueError):
        q2([5, 2])
