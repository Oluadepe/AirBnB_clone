#!/usr/bin/env python3
""""""
# from models.base_model import BaseModel
import json


class FileStorage:
    """serializes and deserializes instances to and from json files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        :return: the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :param obj:
        :return: nothing
        """
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                # for o in objdict.values():
                #     cls_name = o["__class__"]
                #     del o["__class__"]
                #     self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
