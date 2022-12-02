import sqlite3 as sql
class SQLLibrary:
    def __init__(self):
        
        self.con = sql.connect('data_base.db', detect_types=sql.PARSE_COLNAMES)
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS books(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, title TEXT, year INTEGER, author TEXT)"""
            )
        # self.cur.execute(
        #     "CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, phoneNumber, emailAddress)"
        #     )