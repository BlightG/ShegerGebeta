#!/usr/bin/python3
""" Tag Module for shegergebeta project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

food_tag = Table('food_tag', Base.metadata,
                  Column('food_id', String(60), 
                          ForeignKey('foods.id',
                                     onupdate='CASCADE', ondelete='CASCADE'),
                           primary_key=True),
                  Column('tag_id', String(60), 
                          ForeignKey('tags.id',
                                     onupdate='CASCADE', ondelete='CASCADE'),
                           primary_key=True))

class Tag(BaseModel, Base):
    """Tag Class"""
    __tablename__ = 'tags'
    tag_name = Column(String(50), nullable=False, server_default='NULL')