#!/usr/bin/python3
"""Definition"""


class Square:
    """Representation"""
    def __init__(self, size=0):
        if type(size) is int:
            """Initiialization"""
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """CAlculate and return the area of square"""
        return self.__size ** 2
