#!/usr/bin/python3
""" Food Module for shegergebeta project """
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Food(BaseModel, Base):
    """Food Class"""
    __tablename__ = 'foods'
    food_name = Column(String(260), nullable=False, server_default='NULL')
    description = Column(String(1024), nullable=True, server_default='NULL')
    food_image = Column(String(260), nullable=False, server_default='../static/images/shegergebeta.jpg')
    price = Column(Float, nullable=False, server_default='0.0')
    review_date = Column(DateTime, default=datetime.utcnow(), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    # places = relationship('Place', backref='foods')

    def __init__(self, *args, **kwargs):
        """initializes Food"""
        super().__init__(*args, **kwargs)