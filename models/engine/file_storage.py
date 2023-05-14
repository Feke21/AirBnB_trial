#!/usr/bin/python3
""" defines a class called filestorage """
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instance to JSON and vice versa """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets __objects the object with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj
