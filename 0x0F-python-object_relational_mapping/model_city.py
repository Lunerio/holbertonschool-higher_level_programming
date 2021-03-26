#!/usr/bin/python3
""" This module contains a class definition
   and an instance
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ class for cities table with attributes"""
    __tablename__ = 'cities'
    # id is int, autoincrement, not null, and primary key
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    # name is string, not null and max 128 chars
    name = Column(String(128), nullable=False)
    # int, not null, foreign key
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
