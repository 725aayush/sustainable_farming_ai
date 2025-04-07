import sqlite3

def get_db_conn():
    return sqlite3.connect("database/farm.db")
