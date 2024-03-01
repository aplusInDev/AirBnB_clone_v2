from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity


type_storage = getenv('HBNB_TYPE_STORAGE')
if type_storage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

__all__ = ["State", "City", "User", "Place", "Amenity","storage"]
