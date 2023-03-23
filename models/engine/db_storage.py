#!/usr/bin/python3
"""this module regulate the communication
   between the diffrent modules and the database
"""
import os
import models
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.food import Food
from models.place import Place
from models.tag import Tag

class DBstorage:
    """this class manages the storage of shegergebeta components"""
    __engine = None
    __session = None
    SG_MYSQL_USER = os.getenv('SG_MYSQL_USER')
    SG_MYSQL_PWD = os.getenv('SG_MYSQL_PWD')
    SG_MYSQL_HOST = os.getenv('SG_MYSQL_HOST')
    SG_MYSQL_DB = os.getenv('SG_MYSQL_DB')
    SG_ENV = os.getenv('SG_ENV')
    classes = [Place, Tag, Food]

    def __init__(self):
        """Instanciates a new DBstorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(DBstorage.SG_MYSQL_USER,
                                                 DBstorage.SG_MYSQL_PWD,
                                                 DBstorage.SG_MYSQL_HOST,
                                                 DBstorage.SG_MYSQL_DB),
            pool_pre_ping=True)
        if DBstorage.SG_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Instance that querys a database session"""

        if cls is None:
            objs = self.__session.query(Place).all()
            objs.extend(self.__session.query(Tag).all())
            objs.extend(self.__session.query(Food).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}
    
    def new(self, obj):
        """create a new instance os obj"""
        if obj is not None:
            self.__session.add(obj)
    
    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session if obj is not none"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reload all objs"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """ call remove() method on the private
            session attribute (self.__session) """
        self.__session.close()