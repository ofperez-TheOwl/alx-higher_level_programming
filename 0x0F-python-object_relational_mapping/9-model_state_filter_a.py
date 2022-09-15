#!/usr/bin/python3
"""Module : 9-model_state_filter
lists all states that contains "a" from the given database
Usage: ./<file.py> <username> <password> <database_name>
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    # create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    # query for first state object
    for state in session.query(State).filter(
            State.name.like("%a%")).order_by(State.id):
    # another alternative
    # for state in session.query(State).order_by(State.id):
    #    if ("a" in state.name):"""
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()