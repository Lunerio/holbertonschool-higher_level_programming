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
    cursor.execute("SELECT cities.name FROM cities\
                   LEFT JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name=%s\
                   ORDER BY cities.id ASC", (argv[4],))
    # fetch result into variable
    rows = cursor.fetchall()
    # print rows
    data_list = []
    for i in rows:
        data_list.append(i[0])
    print(', '.join(data_list))
    # close cursor and database
    cursor.close()
    database.close()
