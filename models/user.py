#!/usr/bin/python3
"""This module contains the User class for the AirBnB clone"""
from models.base_model import (BaseModel, Base)
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class inherits from BaseModel"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", back_populates="user",
                              cascade="all, delete")
        reviews = relationship(
            "Review", back_populates="user", cascade="all, delete")
