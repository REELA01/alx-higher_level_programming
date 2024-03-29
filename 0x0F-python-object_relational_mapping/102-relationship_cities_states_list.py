#!/usr/bin/python3
"""a script that lists all City objects from the database"""
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
    for instance in se1.query(State).order_by(State.id):
        for c_ins in instance.cities:
            print(c_ins.id, c_ins.name, sep=": ", end="")
            print(" -> " + instance.name)
