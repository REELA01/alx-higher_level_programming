#!/usr/bin/python3
"""list states from database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    ro = curr.fetchall()
    for row in ro:
        print(row)
    curr.close()
    db.close()
