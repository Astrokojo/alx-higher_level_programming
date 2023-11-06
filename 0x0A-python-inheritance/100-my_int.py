#!/usr/bin/python3
"""
This module contains stuff
"""
class MyInt(int):
    """ Custom int class"""

    def __eq__(self, other):
        """function inverts `==`"""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """function inverts `!=`"""
        return super().__eq__(other)
