#!/usr/bin/python3

"""module - return all states with the letter a in their names"""
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1],argv[2],argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)\
                                 .filter(State.name.like("%a%")).all()
    for res in result:
        print("{}: {}".format(res.id, res.name))
    session.close()