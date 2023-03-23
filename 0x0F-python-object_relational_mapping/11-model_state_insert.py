#!/usr/bin/python3

"""module - adding a new element"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

if __name__ == "__main__":

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1],argv[2],argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_object = State(name='Louisiana')
    session.add(new_object)
    session.commit()
    print(new_object.id)
    session.close()