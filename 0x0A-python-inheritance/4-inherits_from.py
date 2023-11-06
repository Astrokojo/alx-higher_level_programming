#!/usr/bin/python3
def inherits_from(obj, a_class):
    """checks if an instance of a class that inherited from,
        the specific class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
