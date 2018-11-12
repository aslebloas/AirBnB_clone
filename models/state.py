#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance"""
        self.name = ''
        super(State, self).__init__(**kwargs)
