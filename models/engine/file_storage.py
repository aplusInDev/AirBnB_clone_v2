#!/usr/bin/python3
"""This module defines a class called FileStorage that represents the base
model to handle storage file"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A class that handles the file storage of objects"""

    # A private class attribute that represents the path to the JSON file
    __file_path = "file.json"
    # A private class attribute that stores all objects by <class name>.id
    __objects = {}

    def all(self, cls=None) -> dict:
        """Returns the dictionary __objects"""
        if cls:
            return {key: value for key, value in self.__objects.items()
                    if isinstance(value, cls)}
        return self.__objects
    
    def delete(self, obj=None) -> None:
        """Delete obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        key: str = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""
        save_dict: dict = {}
        for key, value in self.__objects.items():
            save_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as storage:
            json.dump(save_dict, storage)

    def reload(self) -> None:
        try:
            with open(self.__file_path, encoding="utf-8") as storage:
                data: dict = json.load(storage)

            for key, value in data.items():
                self.new(eval(key.split(".")[0])(**value))
        except FileNotFoundError:
            pass
