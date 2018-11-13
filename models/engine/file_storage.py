#!/usr/bin/python3
"""Module with FileStorage class"""
import json
import os
from datetime import datetime


class FileStorage():
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    def __init__(self):
        """initializes instance"""
        self.__file_path = os.path.abspath("file.json")
        self.__objects = {}

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
                dic = self.__objects
                for k, v in dic.items():
                    if v['__class__'] == "BaseModel":
                        from models.base_model import BaseModel
                        self.__objects[k] = BaseModel(**v)
                    elif v['__class__'] == "State":
                        from models.state import State
                        self.__objects[k] = State(**v)
                    elif v['__class__'] == "City":
                        from models.city import City
                        self.__objects[k] = City(**v)
                    elif v['__class__'] == "Amenity":
                        from models.amenity import Amenity
                        self.__objects[k] = Amenity(**v)
                    elif v['__class__'] == "Place":
                        from models.place import Place
                        self.__objects[k] = Place(**v)
                    elif v['__class__'] == "Review":
                        from models.review import Review
                        self.__objects[k] = Review(**v)
                    elif v['__class__'] == "User":
                        from models.user import User
                        self.__objects[k] = User(**v)

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}
        with open(self.__file_path, "w") as file:
            for k, v in self.__objects.items():
                dictionary[k] = v.to_dict()
            json.dump(dictionary, file)
