#!/usr/bin/python3
"""This module Defines class City to create cities
tables in database
"""

from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City definition and creation of attrributes
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
