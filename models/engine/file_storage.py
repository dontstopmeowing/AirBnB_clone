#!/usr/bin/python3
"""Comment goes here!"""

from models.base_model import BaseModel
import json


class Filestorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj is not None:
            self.__objects["{}.{}"
                           .format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""
        my_list = {}
        for key in self.__objects:
            my_list[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(my_list, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

            for key in data:
                self.__objects[key] = BaseModel(**data[key])

        except:
            pass
