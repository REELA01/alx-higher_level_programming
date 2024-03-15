#!/usr/bin/python3
"""delete all State objects with name containing letter a from database"""
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
        se1.delete(ins1)
    se1.commit()
