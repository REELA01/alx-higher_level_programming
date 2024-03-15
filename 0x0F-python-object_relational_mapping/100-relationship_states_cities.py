#!/usr/bin/python3
"""script create State California with City San Francisco from database"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    se1 = Session()
    nstat = State(name='California')
    ncity = City(name='San Francisco')
    nstat.cities.append(ncity)
    se1.add(nstat)
    se1.add(ncity)
    se1.commit()
