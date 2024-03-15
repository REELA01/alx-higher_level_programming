#!/usr/bin/python3
"""contain State class and Base"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """class with id and name attributes of state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
