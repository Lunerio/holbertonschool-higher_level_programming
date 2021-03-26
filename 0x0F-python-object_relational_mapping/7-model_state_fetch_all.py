#!/usr/bin/python3
""" This module lists objects from db using SQLAlchemy
"""


from sqlalchemy import create_engine, Column
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    #
    Base.metadata.create_all(engine)
    #create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # loop throught items and get query
    for i in session.query(State).order_by(State.id):
        print('{}: {}'.format(i.id, i.name))
    session.close()
