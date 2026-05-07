"""This module contains utility functions."""


def add(a: int, b: int) -> int:
    """This function adds two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """This function subtracts two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """This function multiplies two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """This function divides two numbers."""
    return a / b


def int_to_bin(n: int) -> str:
    """This function converts an integer to binary."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Value must be an integer.")

    if n < 0 or n > 100:
        raise ValueError("Number must be between 0 and 100.")

    return bin(n)[2:]
