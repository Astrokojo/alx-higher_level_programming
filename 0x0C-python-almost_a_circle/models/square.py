#!/bin/usr/python3
"""
Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    model representing a square

    Attributes:
        size (int): Size of the square.
        x (int): x-coordinate of the square.
        y (int): y-coordinate of the square.
        id (int): Unique identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Updates square's attributes

        Args:
            *args: var number of arguments.
            **kwargs: var number of keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
