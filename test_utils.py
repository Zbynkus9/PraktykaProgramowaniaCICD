"""This module contains unit tests for the utils.py module."""

import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    """Test of adding two numbers."""
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """Test of subtracting two numbers."""
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """Test of multiplying two numbers."""
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """Test of dividing two numbers."""
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "n, expected", [(0, "0"), (1, "1"), (5, "101"), (10, "1010"), (100, "1100100")]
)
def test_int_to_bin_correctness(n, expected):
    """Test conversion of integer to binary."""
    assert utils.int_to_bin(n) == expected


@pytest.mark.parametrize("n", [-1, -50, 101, 1000])
def test_int_to_bin_out_of_range(n):
    """Test for integer out of range."""
    with pytest.raises(ValueError):
        utils.int_to_bin(n)


@pytest.mark.parametrize("n", [5.5, -3.14, "10", None])
def test_int_to_bin_not_natural(n):
    """Test for non-natural numbers."""
    with pytest.raises(TypeError):
        utils.int_to_bin(n)
