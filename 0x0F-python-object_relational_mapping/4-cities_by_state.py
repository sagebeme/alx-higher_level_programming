#!/usr/bin/python3

"""module - inner joins sql statement"""
import MySQLdb
from sys import argv

""" a function to use inner joins in mysqldb"""

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute(
            """SELECT cities.id, cities.name, states.name FROM cities INNER
            JOIN states ON cities.state_id =  states.id""")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()