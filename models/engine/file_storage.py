#!/usr/bin/python3
""" the file storage class """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes and deserializes files to JSOn and back """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionart __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects to the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file path """
        x = json.dumps({k: v.to_dict() for k, v in self.__objects.items()})
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(x)

    def reload(self):
        """ deserializes the JSON file to __objects, if path exists or do
        nothing. no exceptions should raise """
        obj_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                    "City": City, "Amenity": Amenity, "Place": Place,
                    "Review": Review}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                if f.read():
                    x = json.loads(f.read())
                    for k, v in x.items():
                        self.__objects[k] = obj_dict[v["__class__"]](**v)
