#!/usr/bin/python3
"""Lists all state objects containing 'a' from the db hbtn_0e_6_usa.
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

    # Query database
    all_states = session.query(State).order_by(
            State.id.asc()).filter(State.name.like('%a%'))
    for state in all_states:
        print("{}: {}".format(state.id, state.name))
