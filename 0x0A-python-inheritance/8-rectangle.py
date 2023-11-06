#!/usr/bin/python3
"""
The file contains the class BaseGeometry and its subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle subclass of base class BaseGeometry"""

    def __init__(self, width, height):
        """instance of a rectangle
            validates if the width and height are integers
        """
        self.integer_validator("width", width)
        self.__width = (width)
        self.integer_validator("height", height)
        self.__height = (height)
