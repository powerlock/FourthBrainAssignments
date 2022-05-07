from src.add import add
import numpy as np
def test_add():
    assert add(1,100) == 101
def test_string():
    assert add("fourth","brain") == "fourthbrain"
def test_array():
    a = np.arange(3)
    b = np.arange(3,6)
    c = np.array([3,5,7])
    assert add(a,b).any() == c.any()
