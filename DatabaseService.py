import sqlite3


class DatabaseService:

    def __init__(self):
        self.connection = sqlite3.connect("Database.db")                # connect to the database

    def execute_command(self, sql_command, params=None):               #
        cursor = self.connection.cursor()
        if params is None:
            cursor.execute(sql_command)
        else:
            cursor.execute(sql_command, params)
        self.connection.commit()
        return cursor.fetchall()

    def close_db_connection(self):
        # close the connection
        self.connection.close()



