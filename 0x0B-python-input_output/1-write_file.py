#!/usr/bin/python3
"""
this module contains write_file function
"""


def write_file(filename="", text=""):
    """ites string to file and returns num of chars written"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
