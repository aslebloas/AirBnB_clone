#!/usr/bin/python3
"""Module with classe BaseModel"""

from datetime import date


class BaseModel():
    """BaseModel Class"""
    def __init__(self, id,
                 created_at=date.today, updated_at=date.today):
        """Initialization of instance
        Args:
             created_at: current datetime when an instance is created
             updated_at: current datetime when an instance is created or updated
        """
        id = self.id
        created_at = self.created_at
        updated_at = self.updated_at

    def __str__(self):
        """prints a summary of the instance attributes"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute upadated_at
        with the current datetime"""
        self.updated_at = datetime.today
