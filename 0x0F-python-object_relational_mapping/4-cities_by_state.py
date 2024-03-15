#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbsql = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dbsql=sys.argv[3], port=3306)
    curr = dbsql.cursor()
    curr.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    ro = curr.fetchall()
    for row in ro:
        print(row)
    curr.close()
    dbsql.close()
