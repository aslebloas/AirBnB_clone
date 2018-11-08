#!/usr/bin/python3
"""Module with FileStorage class"""
import os


class FileStorage():
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    def __init__(self):
        """initializes instance"""
        path = os.path.abspath("file.json")
        if os.path.isfile(path):
            self.__file_path = os.path.abspath("file.json")
        else:
            self.__file_path = None
        self.__objects = {}

    def reload(self):
        """deserializes the JSON file to __objects"""
        if self.__file_path is not None:
            print("file exists")

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object
        """
#        self.__objects = obj


    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
