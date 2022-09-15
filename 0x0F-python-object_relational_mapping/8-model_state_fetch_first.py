#!/usr/bin/python3
"""Module : 8-model_state_fetch_first
prints the first state object from the given database
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
    first_state = session.query(State).order_by(State.id).first()
    if (first_state):
        print("{:d}: {:s}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
