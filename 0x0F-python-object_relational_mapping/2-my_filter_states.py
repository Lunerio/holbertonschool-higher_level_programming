#!/usr/bin/python3
"""This module connects to a database and prints rows
   argv[1] = username
   argv[2] = password
   argv[3] = database name
   argv[4] = Data filter
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
    cur.execute("SELECT * FROM states WHERE name LIKE " +
                "BINARY '{}'".format(argv[4]))
    # fetch result into variable
    rows = cursor.fetchall()
    # print rows
    for i in rows:
        print('{}'.format(i))
    # close cursor and database
    cursor.close()
    database.close()
