#!/usr/bin/python3
"""
This module contains the function read_file
"""


def read_file(filename=""):
    """reads a text file(UTF8) and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
