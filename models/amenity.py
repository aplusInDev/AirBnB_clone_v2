#!/usr/bin/python3
"""This module contains the Amenity class for the AirBnB clone"""
from models.base_model import (BaseModel, Base)
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """This class inherits from BaseModel"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship(
            "Place", secondary="place_amenity", back_populates="amenities")
