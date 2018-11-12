#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """State Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of instance"""
        self.name = ''
        self.city_id = ''
        self.user_id = ''
        self.description = ''
        self.number_bathrooms = 0
        self.number_rooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        if len(kwargs) != 0:
            if "city_id" in kwargs:
                self.city_id = kwargs["city_id"]
            if "user_id" in kwargs:
                self.user_id = kwargs["user_id"]
            if "description" in kwargs:
                self.description = kwargs["description"]
            if "number_rooms" in kwargs:
                self.number_rooms = kwargs["number_rooms"]
            if "number_bathrooms" in kwargs:
                self.number_bathrooms = kwargs["number_bathrooms"]
            if "max_guest" in kwargs:
                self.max_guest = kwargs["max_guest"]
            if "price_by_night" in kwargs:
                self.price_by_night = kwargs["price_by_night"]
            if "latitude" in kwargs:
                self.latitude = kwargs["latitude"]
            if "longitude" in kwargs:
                self.longitude = kwargs["longitude"]
            if "amenity_ids" in kwargs:
                self.amenity_ids = kwargs["amenity_ids"]
        super(City, self).__init__(kwargs)
