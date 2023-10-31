#!/usr/bin/python3
"""
    Integers addition module
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int): First integer.
    b (int, optional): Second integer. Default is 98.

    Returns:
    int: THe sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or a float that cannot be cast to an integer.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
