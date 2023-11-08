#!/usr/bin/python3
"""
Contains the class Student
"""


class Student:
    """A student Class"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dict rep of a Student instance"""
        return self.__dict__
