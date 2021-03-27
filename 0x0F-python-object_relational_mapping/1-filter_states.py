#!/usr/bin/python3
"""This module connects to a database and prints rows
   argv[1] = username
   argv[2] = password
   argv[3] = database name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    # connect to a database
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    # create cursor
    cursor = database.cursor()
    # execute query
    cursor.execute("SELECT * FROM states WHERE\
                   name LIKE 'N%' ORDER BY id ASC")
    # fetch result into variable
    rows = cursor.fetchall()
    # print rows
    for i in rows:
        print(i)
    # close cursor and database
    cursor.close()
    database.close()
