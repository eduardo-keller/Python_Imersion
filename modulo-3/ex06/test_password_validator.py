import password_validator
import pytest

@pytest.mark.parametrize(
    "given, expected",
    [
        ("1", False),
        ("12345678", True),

    ]
)
def test_min_8(given: str, expected: bool) -> None:
    """check min 8 chars"""
    result = password_validator.min_8(given)
    assert result == expected

@pytest.mark.parametrize(
    "given, expected",
    [
        ("123456789123456789", False),
        ("12345678", True),

    ]
)
def test_max_16(given: str, expected: bool) -> None:
    """check max 16 chars"""

@pytest.mark.parametrize(
    "given, expected",
    [
        ("1", False),
        ("12345678", True),

    ]
)
def test_min_8(given: str, expected: bool) -> None:
    """check min 8 chars"""
 
    result = password_validator.max_16(given)
    assert result == expected

@pytest.mark.parametrize(
    "given, expected",
    [
        ("aa", False),
        ("aA", True),

    ]
)
def test_upper(given: str, expected: bool) -> None:
    """check one upper"""
    result = password_validator.upper(given)
    assert result == expected

@pytest.mark.parametrize(
    "given, expected",
    [
        ("AA", False),
        ("aA", True),

    ]
)
def test_lower(given: str, expected: bool) -> None:
    """check one lower"""
    result = password_validator.lower(given)
    assert result == expected

@pytest.mark.parametrize(
    "given, expected",
    [
        ("Aa", False),
        ("a1", True),

    ]
)
def test_has_digit(given: str, expected: bool) -> None:
    """check one digit"""
    result = password_validator.has_digit(given)
    assert result == expected

@pytest.mark.parametrize(
    "given, expected",
    [
        ("Aa", False),
        ("a#", True),

    ]
)
def test_has_special(given: str, expected: bool) -> None:
    """check one special"""
    result = password_validator.has_special(given)
    assert result == expected

@pytest.mark.parametrize(
    "given, expected",
    [
        ("A ", False),
        ("a#", True),

    ]
)
def test_no_spaces(given: str, expected: bool) -> None:
    """check no blank"""
    result = password_validator.no_spaces(given)
    assert result == expected