#!/usr/bin/python3
""" This module deletes objects with letter a with SQLAlchemy
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
    states_to_delete = session.query(State).filter(State.name.like('%a%'))
    for i in states_to_delete:
        session.delete(i)
    session.commit()
    session.close()
