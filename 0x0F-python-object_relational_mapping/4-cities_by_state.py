#!/usr/bin/python3
""" displays all cities table of hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("needs 3 arguments")
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
        cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
                INNER JOIN states \
                    On cities.state_id = states.id \
                        ORDER BY cities.id ASC")

        for state in cur.fetchall():
            print(state)
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
