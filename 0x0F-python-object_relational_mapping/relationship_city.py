#!/usr/bin/python3
"""Module: relationship_city
Defines a class City that inherits from SQLAlchemy's declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey

from relationship_state import Base, State


class City(Base):
    """Definition of a class City that inherits from SQLAlchemy's
    declarative_base. So it's mapped to a MySQL table that's named `cities`
    """

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
