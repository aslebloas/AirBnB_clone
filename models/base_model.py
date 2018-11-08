#!/usr/bin/python3
"""Module with classe BaseModel"""

import uuid
from datetime import date


class BaseModel():
    """BaseModel Class"""
    def __init__(self, id=str(uuid.uuid4()), created_at=date.today, updated_at=date.today):
        """Initialization of instance
        Args:
             created_at: current datetime when an instance is created
             updated_at: current datetime when an instance is created or updated
        """
        self.id = id
        self.created_at = str(created_at)
        self.updated_at = str(updated_at)

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
        #dic = {'id': self.id, '
        dic = self.__dict__
        dic ['__class__'] = self.__class__
        return dic
