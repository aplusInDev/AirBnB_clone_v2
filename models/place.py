#!/usr/bin/env python3
"""This module defines a class called Place
that inherits from BaseModel and represents a place"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


env_value = os.getenv('HBNB_TYPE_STORAGE')
# place_amenity = Table('place_amenity', Base.metadata,
#                       Column('place_id', String(60),
#                              ForeignKey('places.id'),
#                              primary_key=True,
#                              nullable=False),
#                       Column('amenity_id', String(60),
#                              ForeignKey('amenities.id'),
#                              primary_key=True,
#                              nullable=False))


class Place(BaseModel, Base):
    """A class that inherits from BaseModel and represents a place"""

    __tablename__ = "places"
    if env_value == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        # amenities = relationship("Amenity", secondary=place_amenity,
        #                          viewonly=False)
        reviews = relationship("Review", backref='place',
                               cascade="all, delete")
    else:
        city_id: str = ""
        user_id: str = ""
        name: str = ""
        description: str = ""
        number_rooms: int = 0
        number_bathrooms: int = 0
        max_guest: int = 0
        price_by_night: int = 0
        latitude: float = 0.0
        longitude: float = 0.0
        amenity_ids: list = []

        def reviews(self):
            """Getter attribute in case of file storage"""
            from models import storage
            from models.review import Review
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        # @property
        # def amenities(self):
        #     from models import storage
        #     from models.amenity import Amenity
        #     amenities_list = []
        #     for value in storage.all(Amenity).values():
        #         if value.id in self.amenity_ids:
        #             amenities_list.append(value)
        #     return amenities_list

        # @amenities.setter
        # def amenities(self, obj):
        #     from models.amenity import Amenity
        #     if type(obj) == Amenity:
        #         self.amenity_ids.append(obj.id)
