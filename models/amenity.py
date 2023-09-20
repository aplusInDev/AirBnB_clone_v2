#!/usr/bin/python3
"""This module defines a class called Amenity
that handle all Amenity instances"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity
import os


env_value = os.environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel):
    """A class that inherits from BaseModel and represents an amenity"""

    if env_value == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name: str = ""
