#!/usr/bin/python3
"""New Module"""
import json


class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def fromjsonstring(jsonstring):
        """Return list of instances from JSON string representation."""
        if jsonstring is None or jsonstring == "":
            return []
        else:
            return json.loads(jsonstring)

    @classmethod
    def create(cls, dictionary):
        """Return instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def loadfromfile(cls):
        """Return list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
                obj_list = cls.fromjsonstring(json_str)
                return [cls.create(obj_dict) for obj_dict in obj_list]
        except FileNotFoundError:
            return []
