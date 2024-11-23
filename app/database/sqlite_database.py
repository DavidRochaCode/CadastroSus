# database/sqlite_database.py
import sqlite3
from app.database.database_interface import DatabaseInterface

class SQLiteDatabase(DatabaseInterface):
    def __init__(self, database='projetoubs.db'):
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()

    def execute(self, query, params=None):
        self.cur.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=None):
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
