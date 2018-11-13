#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """State Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance"""
        self.name = ''
        super(Amenity, self).__init__(**kwargs)
