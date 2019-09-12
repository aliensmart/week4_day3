import sqlite3
import os

DIR = os.path.dirname(__file__)
DBTABLENAME = "factory.db" 
DBPATH = os.path.join(DIR, DBTABLENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
        SQL = "DROP TABLE IF EXISTS employees;"

        curs.execute(SQL)

        SQL = """CREATE TABLE employees(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            job VARCHAR, 
            years INTEGER,
            department VARCHAR,
            factory_pk INTEGER,
            FOREIGN KEY(factory_pk) REFERENCES factories_compo(pk)

        );"""
        curs.execute(SQL)

        SQL = "DROP TABLE IF EXISTS items;"

        curs.execute(SQL)

        SQL = """CREATE TABLE items(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            explosive BOOL,
            weight FLOAT,
            cost FLOAT,
            factory_pk INTEGER,
            FOREIGN KEY(factory_pk) REFERENCES factories_compo(pk)

        );"""

        curs.execute(SQL)

        SQL = "DROP TABLE IF EXISTS factories_compo;"
        curs.execute(SQL)

        SQL = """CREATE TABLE factories_compo(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            days_since_last_incident INTEGER
        );"""
        curs.execute(SQL)
