#!/usr/bin/python3
"""Module : 100-relationship_states_cities
creates the State “California” with the City “San Francisco”
from a given database
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

    # query to get the cities
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # adding and persisting the object to the database
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
