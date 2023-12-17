#!/usr/bin/python3

"""
This module takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where 'name' matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        port=3306,
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    curr = db.cursor()

    state_name = sys.argv[4]

    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    curr.execute(query, (state_name,))
    all_city = curr.fetchall()
    _len = len(all_city)

    for x in range(_len):
        if x == _len - 1:
            print(all_city[x][0], end="")
        else:
            print(all_city[x][0], end=", ")
    print()

    curr.close()
    db.close()
