#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""
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
    n_state = State(name='Louisiana')
    se1.add(n_state)
    nins1 = se1.query(State).filter_by(name='Louisiana').first()
    print(nins1.id)
    se1.commit()
