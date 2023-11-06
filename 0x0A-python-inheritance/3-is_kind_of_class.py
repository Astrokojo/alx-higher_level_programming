#!/usr/bin/python3
"""
has a class and return true
"""


def is_kind_of_class(obj, a_class):
    """function to check if an object is an instance of a class,
        or if the object is an instance of a class that inherited,
        from the specified class
    """
    return (isinstance(obj, a_class))
