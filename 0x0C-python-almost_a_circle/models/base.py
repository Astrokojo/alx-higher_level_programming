#!/usr/bin/python3
"""
Module has the first class Base
"""
import json


class Base():
    """
    The base model
    Attributes:
        __nb_objects (int): the number of Base instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Creates a base instance
        Args:
            id(int): the identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file in JSON format.

        Args:
            list_objs (list): List of objects to save.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"

        with open(filename, 'w', encoding="utf-8") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(dict_list)
                json_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to convert.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes from a dictionary.

        Args:
            dictionary (dict): Dictionary containing attribute values.

        Returns:
            object: Instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file in JSON format.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as json_file:
                dict_lists = Base.from_json_string(json_file.read())
                return [cls.create(**dict) for dict in dict_lists]
        except FileNotFoundError:
            return []
