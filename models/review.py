#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """State Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance"""
        self.place_id = ''
        self.user_id = ''
        self.text = ''
        if len(kwargs) != 0:
            if "place_id" in kwargs:
                self.place_id = kwargs["place_id"]
            if "user_id" in kwargs:
                self.user_id = kwargs["user_id"]
            if "text" in kwargs:
                self.text = kwargs["text"]
        super(Review, self).__init__(kwargs)
