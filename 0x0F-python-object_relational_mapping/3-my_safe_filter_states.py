#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cmd = """SELECT * FROM states\
        Where Binary name=%s ORDER BY id ASC"""
    cursor.execute(cmd, (argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
