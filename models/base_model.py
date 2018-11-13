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
        if type(kwargs) is dict and len(kwargs) != 0:
            """ LOOP FOR SETTING VALUES """
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v, fmt)
                elif k == "created_at":
                    self.created_at = datetime.strptime(v, fmt)
                else:
                    setattr(self, str(k), v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """prints a summary of the instance attributes"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute upadated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys and values of __dict__
        of the instance """
        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        dic = {}
        dic['__class__'] = str(self.__class__.__name__)
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
