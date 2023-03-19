#!/usr/bin/python3

"""
Database -module import
    """
import sys
import MySQLdb

''' lists all states from the database hbtn_0e_0_usa
    Usage: ./0-select_states.py   <mysql username>\
                                  <mysql password>\
                                  <database name>
'''

if __name__ == "__main__":
    db = MySQLdb.connect(hosts="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]

