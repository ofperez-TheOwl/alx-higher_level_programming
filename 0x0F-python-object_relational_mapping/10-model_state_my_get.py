#!/usr/bin/python3
"""Module : 10-model_state_my_get
prints the state object from a given database with the name passed as argument
Usage: ./<file.py> <username> <password> <database_name> <state_name>
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

    # query for state object
    state = session.query(State).filter_by(name=argv[4]).first()
    if (state):
        print("{:d}".format(state.id))
    else:
        print("Not found")

    session.close()
