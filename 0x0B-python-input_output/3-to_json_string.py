#!/usr/bin/python3
"""
this module contains function to_json_string
"""
import json


def to_json_string(m_obj):
    """returns JSON rep of an obj(str)"""
    return json.dumps(m_obj)
