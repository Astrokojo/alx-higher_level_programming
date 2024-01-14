#!/usr/bin/python3
""" Delete all state objects with the a name containing "a"
from the db hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete Objects
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
