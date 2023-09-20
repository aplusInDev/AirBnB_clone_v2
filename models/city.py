#!/usr/bin/python3
"""This module defines a class called City
that inherits from BaseModel and represents a city"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


env_value = os.environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """A class that inherits from BaseModel and represents a city"""

    __tablename__ = "cities"
    if env_value == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    else:
        name: str = ""
        state_id: str = ""
