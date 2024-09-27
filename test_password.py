import pytest

from password import regex_password_checker


def test_regex_password_checker_valid():
    """Test regex_password_checker with valid passwords."""
    assert regex_password_checker("Password1!") is True
    assert regex_password_checker("Valid$123") is True
    assert regex_password_checker("Test@2021") is True


def test_regex_password_checker_invalid():
    """Test regex_password_checker with invalid passwords."""
    assert regex_password_checker("password") is False
    assert regex_password_checker("PASSWORD") is False
    assert regex_password_checker("12345678") is False
    assert regex_password_checker("Passw1") is False
    assert regex_password_checker("Passw1!") is False
    assert regex_password_checker("Password!") is False
    assert regex_password_checker("Password1") is False
