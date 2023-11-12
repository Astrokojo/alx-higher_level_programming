#!/usr/bin/python3
"""
Module has the first class Base
"""
import json

class Base():
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == [] :
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    def save_to_file(cls, list_objs):
        with open(cls, 'w', encoding="utf-8") as file:
            json.dump(list_objs, file)
