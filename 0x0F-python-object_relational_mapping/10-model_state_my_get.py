#!/usr/bin/python3
"""script that prints the State object with the name passed as argument"""
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
    ins1 = se1.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(ins1[0].id)
    except IndexError:
        print("Not found")