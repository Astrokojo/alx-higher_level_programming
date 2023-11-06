#!/usr/bin/python3
"""
    module contains the rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size):
        """validated instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of suqare"""
        return self.__size * self.__size

    def __str__(self):
        """informal string"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
