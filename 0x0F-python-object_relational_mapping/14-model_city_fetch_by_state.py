#!/usr/bin/python3
"""prints all City objects by state from database hbtn_0e_14_usa"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    import sqlalchemy
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    USR = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]
    conn_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(USR,
                                                              PWD,
                                                              DB)
    engine = create_engine(conn_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city in cities:
        print('{}: ({}) {}'.format(city.State.name,
                                   city.City.id, city.City.name))
