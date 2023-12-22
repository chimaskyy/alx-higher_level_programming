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

    state_name = sys.argv[4]

    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
