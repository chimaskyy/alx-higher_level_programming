#!/usr/bin/python3

"""
This modelue lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
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

    curr.execute("SELECT * FROM states WHERE\
            name LIKE BINARY 'N%'" "ORDER BY id ASC")
    states = curr.fetchall()

    for state in states:
        print(state)

    curr.close()
    db.close()
