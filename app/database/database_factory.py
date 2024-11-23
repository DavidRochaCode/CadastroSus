# database/database_factory.py
from app.database.postgresql_database import PostgreSQLDatabase
from app.database.sqlite_database import SQLiteDatabase

class DatabaseFactory:
    @staticmethod
    def create_database(db_type='postgresql', **kwargs):
        if db_type == 'postgresql':
            return PostgreSQLDatabase(**kwargs)
        elif db_type == 'sqlite':
            return SQLiteDatabase(**kwargs)
        else:
            raise ValueError(f"Tipo de banco de dados '{db_type}' não suportado.")
