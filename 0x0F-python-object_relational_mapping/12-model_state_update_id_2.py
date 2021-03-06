#!/usr/bin/python3
""" This module changes name of element with SQLAlchemy
"""


from sqlalchemy import create_engine, Column
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # get id
    state_to_update = session.query(State).get(2)
    state_to_update.name = 'New Mexico'
    session.commit()
    session.close()
