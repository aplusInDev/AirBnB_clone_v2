#!/usr/bin/python3
""" This module defines a class called DBStorage that represents the
database storage engine for the AirBnB clone project.
"""

from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


classes_list = [User, State, City, Place, Review, Amenity]

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes a new instance of the DBStorage class"""
        env = getenv('HBNB_ENV')
        mysql_user = getenv('HBNB_MYSQL_USER', 'hbnb_dev')
        mysql_pwd = getenv('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
        mysql_host = getenv('HBNB_MYSQL_HOST', 'localhost')
        mysql_db = getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')
        type_storage = getenv('HBNB_TYPE_STORAGE')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(mysql_user, mysql_pwd,
                                             mysql_host, mysql_db),
                                      pool_pre_ping=False)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the dictionary __objects"""

        if cls and cls in classes_list:
            query_list = self.__session.query(cls).all()
        else:
            query_list = []
            for cls in classes_list:
                query_list.extend(self.__session.query(cls).all())
        obj = {type(obj).__name__ + '.' + obj.id: obj for obj in query_list}
        return obj

    def new(self, obj):
        """This method adds the specified object to the current database
        session
        """
        self.__session.add(obj)

    def save(self):
        """This method commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This method deletes the specified object from the current database
        session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """This method creates all tables in the database and initializes a
        new session with the current database engine
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """This method calls remove() on the private session attribute
        (self.__session) or close() on the class Session"""
        self.__session.remove()
