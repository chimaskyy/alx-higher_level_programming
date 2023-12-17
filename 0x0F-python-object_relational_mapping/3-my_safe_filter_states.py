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

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    curr.execute(query, (state_name,))
    states = curr.fetchall()

    for state in states:
        print(state)

    curr.close()
    db.close()
