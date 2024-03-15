#!/usr/bin/python3
"""print the first State object from database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    se1 = Session()
    for ins1 in se1.query(State).filter(State.name.like('%a%')):
        print(ins1.id, ins1.name, sep=": ")
