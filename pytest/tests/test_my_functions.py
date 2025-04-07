import pytest
import src.my_functions as my_functions


def test_add():
    result = my_functions.add(2, 3)
    assert result == 5
    
def test_subtract():
    result = my_functions.subtract(5, 3)
    assert result == 2
    
def test_divide():
    result = my_functions.divide(6, 3)
    assert result == 2.0
    
    
def add_strings():
    result = my_functions.add("Hello, ", "world!")
    assert result == "Hello, world!"
