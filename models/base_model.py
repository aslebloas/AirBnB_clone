#!/usr/bin/python3
"""Module with classe BaseModel"""

import uuid
from datetime import date


class BaseModel():
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance
        Args:
             created_at: current datetime when an instance is created
             updated_at: current datetime when an instance is created or updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(date.today)
        self.updated_at = str(date.today)
        if len(kwargs) != 0:
            """ LOOP FOR SETTING VALUES """
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "my_number":
                    self.my_number = v
                if k == "__class__":
                    self.__class__ = v
                if k == "updated_at":
                    """ NEED TO MAKE THESE DATETIME"""
                    self.updated_at = v
                if k == "created_at":
                    self.created_at = v
                if k == "name":
                    self.name = v

    def __str__(self):
        """prints a summary of the instance attributes"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute upadated_at
        with the current datetime"""
        self.updated_at = date.today

    def to_dict(self):
        """ returns a dictionary containing all keys and values of __dict
        of the instance """
        dic = self.__dict__
        if ! dic['class']:
            dic ['__class__'] = self.__class__
        return dic
