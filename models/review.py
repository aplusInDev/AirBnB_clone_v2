#!/usr/bin/env python3
"""This module defines a class called Review
that inherits from BaseModel and represents a review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that inherits from BaseModel and represents a review"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
