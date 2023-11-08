#!/usr/bin/python3
"""
module contains from_json_string
"""
import json


def from_json_string(my_str):
    """returns an object(Python data structure) rep'd by a JSON string"""
    return json.loads(my_str)
