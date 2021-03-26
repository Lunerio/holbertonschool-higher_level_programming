#!/usr/bin/python3
""" This module prints cities from City
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # query with join
    cities_states = session.query(City, State).\
        join(State).filter().order_by(City.id).all()
    for i, j in cities_states:
        print('{}: ({}) {}'.format(j.name, i.id, i.name))
