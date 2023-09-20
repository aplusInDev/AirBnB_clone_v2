#!/usr/bin/python3
"""Review of the HBNB Project Module: """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

env_value = os.environ.get("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review class """

    if env_value == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        text: str = ""
        place_id: str = ""
        user_id: str = ""
