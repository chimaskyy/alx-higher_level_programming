#!/usr/bin/python3
"""This module lists all states from the
database named hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

        cur.close()
        db.close()
