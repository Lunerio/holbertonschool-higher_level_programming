#!/usr/bin/python3
""" This module adds element to table with SQLAlchemy
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
    # create object
    louisiana = State(name="Louisiana")
    # add object to table
    session.add(louisiana)
    session.commit()
    # print the new id
    print(louisiana.id)
    session.close()
