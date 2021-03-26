#!/usr/bin/python3
""" This module lists objects from db using SQLAlchemy
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
    # query state from arguments
    state_id = session.query(State).filter(State.name.like(argv[4]))
    # loop to get the id if exists
    # flag to find if it exists
    found = False
    for i in state_id:
        if i.name == argv[4]:
            print('{}'.format(i.id))
            found =  True
            break
    if found is False:
        print('Not found')
    session.close()
