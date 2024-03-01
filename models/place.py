#!/usr/bin/python3
"""This module contains the Place class for the AirBnB clone"""
from models.base_model import (BaseModel, Base)
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', ondelete='cascade',
                                            onupdate='cascade'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id',
                                            ondelete='cascade',
                                            onupdate='cascade'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This class inherits from BaseModel"""
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey('cities.id', ondelete='cascade',
                                onupdate='cascade'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', ondelete='cascade',
                                onupdate='cascade'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates="places")
        user = relationship("User", back_populates="places")

        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """Returns a list of review instances with place_id equal to the
            current Place.id
            """
            from models import storage

            review_list = []
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns a list of Amenity instances with place_id equal to the
            current Place.id
            """
            from models import storage

            amenity_list = []
            for amenity in storage.all("Amenity").values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Sets the amenities attribute to a given Amenity instance"""
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
            else:
                return
