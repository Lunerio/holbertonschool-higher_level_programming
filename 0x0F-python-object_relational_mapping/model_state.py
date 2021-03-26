#!/usr/bin/python3
""" This module contains a class definition
   and an instance
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# instance of declarative_base
Base = declarative_base()


class State(Base):
    """ class for states table with attributes"""
    __tablename__ = 'states'
    # id is int, autoincrement, not null, and primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    # name is string, not null and max 128 chars
    name = Column(String(128), nullable=False)
