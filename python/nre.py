import sqlite3

class Database:
    def __init__(self, dbSQLite):
        self.conn = sqlite3.connect(dbSQLite)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTIS partes(id INTEGER PRIMARY KEY, part text, retailer text, price")
        self.conn.commit()

        def fetch(self):
            self.cur.exevute("select * from partes")
            rows = self.cur.fetcha11()
            return rows


        def insert (self,part,custumer,retailer,price):
            elf.