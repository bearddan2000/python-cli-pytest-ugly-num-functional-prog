import pytest
import main

def test_max_divide():
    assert main.max_divide(10, 5) == 2

def test_is_ugly():
    assert main.is_ugly(0, [2,3,5], 12) == True

def test_find_ugly():
    assert main.find_ugly(10, 1, 1, [2,3,5]) == 12
