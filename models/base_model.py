#!/usr/bin/python3
"""Base class Definition"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ BaseModel definition"""

    def __init__(self, *args, **kwargs):
        """init method to initialize the values"""
        if (kwargs):
            for k, v in kwargs.items():
                if (k == 'created_at' or k == 'updated_at'):
                    setattr(self, k, datetime.strptime(
                          v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == '__class__':
                    pass
                else:

                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ method to format BaseModel for printing"""
        thestr = "[{:s}] ({:s}) {}".format(
              type(self).__name__, self.id, self.__dict__)
        return thestr

    def save(self):
        """method to save the object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """make dictionary with instance attributes"""
        temp_dict = {}
        temp_dict['__class__'] = type(self).__name__
        for k, v in self.__dict__.items():
            if k == 'created_at':
                temp_dict[k] = v.isoformat()
            elif k == 'updated_at':
                temp_dict[k] = v.isoformat()
            else:
                temp_dict[k] = v
        return temp_dict
