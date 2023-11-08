#!/usr/bin/python3
"""
this module contains append_write function
"""


def append_write(filename="", text=""):
    """appends string to file and returns num of chars written"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
