#!/usr/bin/python3
"""This module contains the City class for the AirBnB clone"""
from models.base_model import (BaseModel, Base)
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """This class inherits from BaseModel"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="cascade",
                                 onupdate="cascade"),
                      nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state = relationship("State", back_populates="cities")
        places = relationship(
            "Place", back_populates="cities", cascade="all, delete", lazy="dynamic")
