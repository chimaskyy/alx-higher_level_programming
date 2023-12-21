#!/usr/bin/python3
""" This module lists all State
instance from the database"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker, Session
    from model_state import Base, State
    import sys

    con = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
