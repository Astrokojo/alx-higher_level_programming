#!/usr/bin/python3
"""Defines a State Model.
Inherits from SQlAlchemy base and links to the MYSQl tables states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQl database.
    Atrributes:
        __tablename__(str): The name of the MySQl table to store states.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
