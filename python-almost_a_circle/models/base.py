#!/usr/bin/python3
"""New Module"""


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
    def savetofile(cls, listobjs):
        """Write JSON string representation of listobjs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            json_str = cls.to_json_string(
                    [obj.to_dictionary() for obj in listobjs])
            file.write(json_str)

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
