#!/usr/bin/env python3
"""This module defines a class called User
that inherits from BaseModel and represents a user"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

env_value = os.getenv('HBNB_TYPE_STORAGE')


class User(BaseModel):
    """A class that inherits from BaseModel and represents a user"""

    if env_value == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref='user', cascade="all, delete")
        reviews = relationship("Review", backref='user', cascade="all, delete")
    else:
        email: str = ""
        password: str = ""
        first_name: str = ""
        last_name: str = ""
