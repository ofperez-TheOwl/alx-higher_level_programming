#!/usr/bin/python3
"""Module : 4-cities_by_states
lists all states from the given database
Usage: ./0-select_states <username> <password> <database_name>
"""


from sys import argv
import MySQLdb as _db

if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    dtbase = _db.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    pointer = dtbase.cursor()
    pointer.execute("SELECT cities.id, cities.name, states.name\
                     FROM states\
                     INNER JOIN cities ON states.id = cities.state_id\
                     ORDER BY cities.id ASC")
    table_rows = pointer.fetchall()
    for row in table_rows:
        print(row)
    pointer.close()
    dtbase.close()
