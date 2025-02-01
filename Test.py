
# Test scripts

import pytest

def sum(a,b):
    return a + b

def test_sum():
    assert sum(1,2) == 3
    assert sum(2,3) == 6
    
test_sum()