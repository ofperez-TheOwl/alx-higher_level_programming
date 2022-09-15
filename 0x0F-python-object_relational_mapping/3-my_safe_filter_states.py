#!/usr/bin/python3
"""Module : 2-my_safe_filter_states
lists all states from the given database which names respect given patterns
Usage: ./<file.py> <username> <password> <database_name> <pattern>
"""


from sys import argv
import MySQLdb as _db

if __name__ == "__main__":
    username, password, database_name = argv[1], argv[2], argv[3]
    dtbase = _db.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    pointer = dtbase.cursor()
    pointer.execute("SELECT * FROM states\
                     WHERE name LIKE %s\
                     ORDER BY id ASC", (argv[4],))
    table_rows = pointer.fetchall()
    for row in table_rows:
        print(row)
    pointer.close()
    dtbase.close()
