#!/usr/bin/python3
""" Tag Module for shegergebeta project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Tag(BaseModel, Base):
    """Tag Class"""
    __tablename__ = 'tags'
    tag_name = Column(String(50), nullable=False, server_default='NULL')
    food = relationship("Food")

    def __init__(self, *args, **kwargs):
        """initializes Tag"""
        super().__init__(*args, **kwargs)