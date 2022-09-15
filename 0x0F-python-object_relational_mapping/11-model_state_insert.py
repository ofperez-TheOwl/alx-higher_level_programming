#!/usr/bin/python3
"""Module : 11-model_state_insert
inserts a new state object into a given database
prints the new state object id
Usage: ./<file.py> <username> <password> <database_name>
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    # create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new object state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{:d}".format(new_state.id))

    session.close()
