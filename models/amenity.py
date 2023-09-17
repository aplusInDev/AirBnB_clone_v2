#!/usr/bin/python3
"""This module defines a class called Amenity
that handle all Amenity instances"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that inherits from BaseModel and represents an amenity"""

    name: str = ""
