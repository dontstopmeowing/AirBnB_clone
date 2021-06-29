#!/usr/bin/python3
"""This file contains the Filestorage class"""

from models.base_model import BaseModel
from models.user import User
import json
classes = {
    "BaseModel": BaseModel,
    "User": User
}


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
                f = json.load(file)

            for key in f:
                self.__objects[key] = classes[f[key]["__class__"]](**f[key])

        except:
            pass

    def find_object(cls, id):
        """ Return object id """
        objs = cls.__objects
        for obj in objs.values():
            if obj.id == id:
                return obj
