#!/usr/bin/python3
"""Module : 7-model_state_fetch_all
lists all state object from the given database
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

    Session = sessionmaker(bind=engine)
    session = Session()
    # query for state objects
    for state in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
