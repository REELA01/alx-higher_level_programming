#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    se1 = Session()
    for ins1 in (se1.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(ins1[0] + ": (" + str(ins1[1]) + ") " + ins1[2])
