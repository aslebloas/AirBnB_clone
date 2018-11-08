#!/usr/bin/python3
"""Module with classe BaseModel"""

import uuid
from datetime import datetime

class BaseModel():
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance
        Args:
             created_at: current datetime when an instance is created
             updated_at: current datetime when an instance is created or updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.today())
        self.updated_at = str(datetime.today())

    def __str__(self):
        """prints a summary of the instance attributes"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute upadated_at
        with the current datetime"""
        self.updated_at = str(datetime.today())

    def to_dict(self):
        """ returns a dictionary containing all keys and values of __dict__
        of the instance """
        dic = self.__dict__
        if '__class__' not in dic:
            dic['__class__'] = str(self.__class__)
        return dic
