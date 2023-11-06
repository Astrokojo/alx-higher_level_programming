#!/usr/bin/python3
"""
    this module contains the base class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class Square"""
    def __init__(self, size):
        """ creates a validated instance of square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2
