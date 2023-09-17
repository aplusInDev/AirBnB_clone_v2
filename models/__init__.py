#!/usr/bin/python3
"""init file for modules package that create an instance of FileStorage class
and call the reload method to deserialize the JSON file to objects"""

from models.engine.file_storage import FileStorage

storage: FileStorage = FileStorage()
storage.reload()
