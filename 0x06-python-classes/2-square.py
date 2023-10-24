#!/usr/bin/python3
"""A class called Square"""


class Square:
    """Represents Square"""
    def __init__(self, size=0):
        """Initializes the square"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
            else:
                raise TypeError('size must be an integer')
