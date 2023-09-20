#!/usr/bin/python3
"""init file for modules package that create an instance of FileStorage class
and call the reload method to deserialize the JSON file to objects"""


import os


env_value = os.environ.get("HBNB_TYPE_STORAGE")


if env_value == "db":
    from models.engine.db_storage import DBStorage

    storage: DBStorage = DBStorage()
else:
    from models.engine.file_storage import FileStorage

    storage: FileStorage = FileStorage()
storage.reload()
