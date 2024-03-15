#!/usr/bin/python3
"""list all State object,and corresponding City object,contained in datbase"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    se1 = Session()
    for instnace in se1.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for c_ins1 in instance.cities:
            print("    ", end="")
            print(c_ins1.id, c_ins1.name, sep=": ")
