#!/usr/bin/python3
"""
Delete the State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # Create engine and connect to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db), pool_pre_ping=True,
                           echo=True, future=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete the State object from the database hbtn_0e_6_usa
    states = Session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()

    # Session close
    session.close()
