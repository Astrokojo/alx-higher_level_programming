#!/usr/bin/python3
"""
List all cities of a particular state from the db hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],)
    cur = db.cursor()
    cur.execute("SELECT states.name, cities.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    all_states = cur.fetchall()
    print(", ".join([cities[1]
                     for cities in all_states
                     if sys.argv[4] == cities[0]]))
    cur.close()
    db.close()
