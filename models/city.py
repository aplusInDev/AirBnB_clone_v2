#!/usr/bin/python3
"""This module defines a class called City
that inherits from BaseModel and represents a city"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that inherits from BaseModel and represents a city"""

    state_id: str = ""
    name: str = ""
