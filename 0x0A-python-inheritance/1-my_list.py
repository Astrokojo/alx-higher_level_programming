#!/usr/bin/python3
"""
Has Mylist class
"""


class MyList(list):
    """
    A custom class that inherits from the list class
        and gives a method to print the list in sorted order

    Public Methods:
        - printed_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
