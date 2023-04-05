#!/usr/bin/python3
""" this module defines a base class for all models of our class"""
import uuid
import models
import datetime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

# used to manage tables
Base = declarative_base()

class BaseModel:
    """A base class for shegerGebeta objects"""
    id = Column(String(60), nullable=False,
                unique=True, primary_key=True)

    def __init__(self, *args, **kwargs):
        """Instatiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
        else:
            try:
                isinstance(kwargs['id'], str)
            except KeyError:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)
        models.storage.new(self)

    def __str__(self):
        """Retruns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        str_dict = self.__dict__.copy()
        if '_sa_instance_state' in str_dict.keys():
            str_dict.pop('_sa_instance_state')
        return '[{}] ({}) {}'.format(cls, self.id, str_dict)

    def save(self):
        """saves an object into storage"""
        models.storage.save()

    def to_dict(self):
        """Converts instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if '_sa_instance_state' in dictionary.keys():
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """Delete the current instance from stroage"""
        models.storage.delete(self)
