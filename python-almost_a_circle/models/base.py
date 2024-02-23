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
        list_dictionaries = None
        if list_objs is not None:
            list_dictionaries = []
            for obj in list_objs:
                list_dictionaries += [obj.to_dictionary()]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(jsonstring):
        """Return list of instances from JSON string representation."""
        if jsonstring is None or jsonstring == "":
            return []
        else:
            return json.loads(jsonstring)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        try:
            dummy_instance.update(**dictionary)
        except (TypeError, ValueError) as e:
            pass
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                if not dict_list:
                    return []
                instances = []
                for dict_obj in dict_list:
                    try:
                        instance = cls.create(**dict_obj)
                        instances.append(instance)
                    except (TypeError, ValueError) as e:
                        print(f"Error creating instance: {e}")
                return instances
        except FileNotFoundError:
            return []
        except (IOError, json.JSONDecodeError) as e:
            return []