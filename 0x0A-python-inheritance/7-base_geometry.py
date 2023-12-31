#!/usr/bin/python3
"""
has a class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """nonfunctional function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if the value is an int"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
