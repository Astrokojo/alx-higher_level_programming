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
    
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            json_file.write("[]")
            
        filename = cls.__name__ + ".json"
        
        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        
        json_str = cls.to_json_string(dict_list)
        
        with open(filename, 'w', encoding="utf-8") as json_file:
            json_file.write(json_str) 
                
