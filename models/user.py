#!/usr/bin/env python3
"""This module defines a class called User
that inherits from BaseModel and represents a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class that inherits from BaseModel and represents a user"""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
