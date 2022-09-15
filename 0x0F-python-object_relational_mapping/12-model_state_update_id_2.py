#!/usr/bin/python3
"""Module : 12-model_state_update_id_2
changes the name of a state object from a given database
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

    # query to get the state and update it
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
