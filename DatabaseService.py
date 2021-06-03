import sqlite3


class DatabaseService:

    def __init__(self):
        self.connection = sqlite3.connect("Database.db")

    def execute_command(self, sql_command):
        cursor = self.connection.cursor()
        cursor.execute(sql_command)
        self.connection.commit()
        return cursor.fetchall()

    def close_db_connection(self):
        self.connection.close()



