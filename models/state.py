#!/usr/bin/python3
"""This module defines a class called State
that inherits from BaseModel and represents a state"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.city import City


env_value = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """A class that inherits from BaseModel and represents a state"""

    __tablename__ = "states"
    if env_value == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name: str = ""

        # @property
        # def cities(self):
        #     """Getter attribute in case of file storage"""
        #     from models import storage
        #     cities_list = []
        #     for city in storage.all(City).values():
        #         if city.state_id == self.id:
        #             cities_list.append(city)
        #     return cities_list
