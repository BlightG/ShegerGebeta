#!/usr/bin/python3
""" Place Module for shegergebeta project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Place Class"""
    __tablename__ = 'places'
    name = Column(String(250), nullable=False, server_default="NULL")
    Location_link = Column(String(250), nullable=False, 
                    server_default="https://www.google.com/maps/@9.0358058,38.7533829,17.94z")
    Longtiude = Column(Float, nullable=False, default=9.0358058)
    Latitude = Column(Float, nullable=False, default=38.7533829)
    foods = relationship('Food')

    def __init__(self, *args, **kwargs):
        """initializes Food"""
        super().__init__(*args, **kwargs)
    