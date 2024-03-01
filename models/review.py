#!/usr/bin/python3
"""This module contains the Review class for the AirBnB clone"""
from models.base_model import (BaseModel, Base)
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """This class inherits from BaseModel"""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60),
                      ForeignKey('places.id', ondelete='cascade',
                                 onupdate='cascade'), nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', ondelete='cascade',
                                onupdate='cascade'), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
