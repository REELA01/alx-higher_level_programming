#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbsql = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dbsql=sys.argv[3], port=3306)
    curr = dbsql.cursor()
    curr.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    ro = curr.fetchall()
    cur = list(row[0] for row in ro)
    print(*cur, sep=", ")
    curr.close()
    dbsql.close()
