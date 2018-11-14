#!/usr/bin/python3
"""Module for class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class with class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def init(self):
        """init with dictionary"""
        super().__init__(**kwargs)
