#!/usr/bin/python3
"""
The file contains the class BaseGeometry and its subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """instance of a rectangle"""
        self.integer_validator("width", width)
        self.__width = (width)
        self.integer_validator("height", height)
        self.__height = (height)

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string rep of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
