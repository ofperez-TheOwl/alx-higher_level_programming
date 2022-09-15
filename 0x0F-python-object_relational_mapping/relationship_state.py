#!/usr/bin/python3
"""Module: relationship_state
Defines a class State that inherits from SQLAlchemy's declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Definition of a State class that inherits from SQLAlchemy's
    declarative_base. So it's mapped to a MySQL table that's named `states`
    """

    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
