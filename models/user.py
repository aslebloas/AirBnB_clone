#!/usr/bin/python3
"""Module for class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    def __init__(self, *args, **kwargs):
        """Instance initialization"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

        super().__init__(**kwargs)
