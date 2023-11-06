#!/usr/bin/python3
"""
has is_same_class class
"""


def is_same_class(obj, a_class):
    """ return true is obj is exactly an instance of the specifieed class."""
    return type(obj) is a_class
