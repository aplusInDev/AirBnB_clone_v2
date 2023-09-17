#!/usr/bin/env python3
"""This module defines a class called Place
that inherits from BaseModel and represents a place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """A class that inherits from BaseModel and represents a place"""

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
