import pytest
from app.numbers import validate_number

def test_digits_only():
    """Test validation with non-digit characters"""
    assert not validate_number("12a4") == True

def test_lenght():
    """Test validation with incorrect length"""
    assert not validate_number("123")
    assert not validate_number("12345")

def test_unique_digits():
    """Test validation with repeated digits"""
    assert not validate_number("1123") == True
    assert not validate_number("1233") == True