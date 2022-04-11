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
    cursor.execute("SELECT cities.name \
                    FROM states \
                    INNER JOIN cities ON states.id = cities.state_id \
                    WHERE Binary states.name=%s \
                    ORDER BY cities.id ASC", (argv[4],))
    res = []
    for row in cursor.fetchall():
        res.append(row)

    for i in range(len(res)):
        res[i] = str(res[i])
        res[i] = res[i].strip(')')
        res[i] = res[i].strip('(')
        res[i] = res[i].strip("'")
        res[i] = res[i].strip(",")
        res[i] = res[i].strip("'")
    res = ', '.join(res)
    print(res)
    cursor.close()
    db.close()
