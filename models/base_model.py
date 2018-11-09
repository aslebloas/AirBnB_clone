#!/usr/bin/python3
"""Module with classe BaseModel"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance
        Args:
            *args: arguments
            **kwargs: keyword arguments
        """
        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        if len(kwargs) != 0:
            """ LOOP FOR SETTING VALUES """

            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "my_number":
                    self.my_number = v
                if k == "__class__":
                    self.__class__ = type(self)
                if k == "name":
                    self.name = v
                if k == "updated_at":
                    """ NEED TO MAKE THESE DATETIME"""
                    self.updated_at = datetime.strptime(v, fmt)
                if k == "created_at":
                    self.created_at = datetime.strptime(v, fmt)

    def __str__(self):
        """prints a summary of the instance attributes"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute upadated_at
        with the current datetime"""
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys and values of __dict__
        of the instance """
        dic = self.__dict__
        if '__class__' not in dic:
            dic['__class__'] = str(self.__class__)
        return dic
