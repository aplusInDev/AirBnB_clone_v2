#!/usr/bin/python3
"""
This module defines a class called BaseModel that represents the base
model for all other classes in the project.
"""

import models
from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel:
    """This class is the base class for all other classes in this project"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This method initializes a new instance of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if kwargs.get("id", None) is None:
                    self.id = str(uuid.uuid4())
                if kwargs.get("created_at", None) is None:
                    if kwargs.get("updated_at", None) is None:
                        self.updated_at = datetime.now()
                    self.created_at = self.updated_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This method returns a string representation of the BaseModel
        instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.to_dict())

    def save(self):
        """This method updates the updated_at attribute with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary representation of the BaseModel
        instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """This method deletes the current instance from the storage"""
        models.storage.delete(self)
