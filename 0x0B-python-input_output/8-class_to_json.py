#!/usr/bin/python3
"""
module has class_to_json function
"""


def class_to_json(obj):
    """returns dict description of obj"""
    return obj.__dict__
