#!/usr/bin/python3
"""This module defines a class called State
that inherits from BaseModel and represents a state"""

from models.base_model import BaseModel


class State(BaseModel):
    """A class that inherits from BaseModel and represents a state"""

    name: str = ""
