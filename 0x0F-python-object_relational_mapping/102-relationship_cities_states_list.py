#!/usr/bin/python3
"""Module : 102-relationship_states_cities_list
lists all City objects from a given database
Usage: ./<file.py> <username> <password> <database_name>
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    # create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query to get the cities' object
    for city in session.query(City).order_by(City.id).all():
        print("{:d}: {:s} -> {:s}".format(
              city.id, city.name, city.state.name))

    # closing the database
    session.close()
