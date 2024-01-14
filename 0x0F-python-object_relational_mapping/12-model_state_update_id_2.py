#!/usr/bin/python3
"""Update the state object where state.id = 2 to the db hbtn_0e_6_usa.
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

    # Updating Objects
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
