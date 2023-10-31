#!/usr/bin/python3
class Rectangle:
    """ a rectangle class """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if type(value) is int:
            self.__width = value
        else:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    def height(self):
        return self.__height

    def height(self, value):
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
