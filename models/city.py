#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """State Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance"""
        self.name = ''
        self.state_id = ''
        if len(kwargs) != 0:
            if "name" in kwargs:
                self.name = kwargs["name"]
            if "state_id" in kwargs:
                self.state_id = kwargs["state_id"]
        super(City, self).__init__(kwargs)
