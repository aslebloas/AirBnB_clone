#!/usr/bin/python3


class FileStorage():
    """ setializes instances to a JSON file and deserializes
    JSON file to instances """

    @property
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj

    def save(self):
        

    def reload(self):

    
