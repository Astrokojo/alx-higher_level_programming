#!/usr/bin/python3
""" displays all values in the states \
        table of hbtn_0e_0_usa where na,e mathces argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("needs 4 arguments")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )

        cur = db.cursor()
        query = ("SELECT * FROM states \
                WHERE `name` = '{}'".format(sys.argv[4]))

        for state in cur.fetchall():
            if state
            print(state)
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
