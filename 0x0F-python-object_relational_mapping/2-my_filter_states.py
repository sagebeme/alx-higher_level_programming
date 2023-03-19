#!/usr/bin/python3

"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./2-myfilter.py  <mysql username>\
                        <mysql password>\
                        <database name>
                        <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",port = 3306, user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
            FROM `states`\
            WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]

db.close()

