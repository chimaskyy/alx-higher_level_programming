#!/usr/bin/python3
""" This module prints state object with the
name passed as argumment"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker, Session
    from model_state import Base, State
    import sys

    # connect mysql db using SqlAlchemy using mysqldb as driver
    con = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])

    # create connection to db
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    new_ = session.new

    if new_state:
        print(new_state.id)
    session.close()
