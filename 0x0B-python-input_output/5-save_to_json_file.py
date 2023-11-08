#!/usr/bin/python3
"""
module contains save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON rep"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
