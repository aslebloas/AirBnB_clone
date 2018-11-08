#!/usr/bin/python3
"""Module with FileStorage class"""


class FileStorage():
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    def __init__(self, file_path, objects):
        """initializes instance"""
        self.__file_path = file_path
        self.__objects = objects

    def reload(self):
        """deserializes the JSON file to __objects"""

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object
        """
        self.__objects = obj


    def save(self)
