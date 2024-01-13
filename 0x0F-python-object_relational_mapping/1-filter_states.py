#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("lists all states with a name starting with `N` from hbtn_0e_0_usa")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
        for state in cur.fetchall():
            print(state)
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
