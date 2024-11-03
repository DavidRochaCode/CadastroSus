import psycopg2

class Database:
    def __init__(self, hostname='localhost', database='projetoubs', username='postgres', pwd='postgres', port_id=5432):
        self.conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
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
