#!/usr/bin/python3
"""Module : 5-filter_cities
lists all cities of a given state from the given database
Usage: ./<file.py> <username> <password> <database_name> <state_name>
"""


from sys import argv
import MySQLdb as _db

if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    dtbase = _db.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    pointer = dtbase.cursor()
    pointer.execute("SELECT cities.name FROM cities\
                     INNER JOIN states ON states.id = cities.state_id\
                     WHERE states.name LIKE %s\
                     ORDER BY cities.id ASC", (argv[4],))
    table_rows = pointer.fetchall()
    print(", ".join(["{:s}".format(row[0]) for row in table_rows]))
    pointer.close()
    dtbase.close()
