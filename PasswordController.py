from DatabaseService import DatabaseService
import pandas as pd


class PasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_password_table(self):
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      password(password_nr INTEGER PRIMARY KEY , title VARCHAR, username VARCHAR, password VARCHAR)""")

    def insert_data(self, title, username, password):
        self.service.execute_command(f"INSERT INTO password (title, username, password) VALUES (?, ?, ?)", (title, username, password))

    def read_data(self, password_nr):
        return self.service.execute_command(f"SELECT * FROM password WHERE password_nr = {str(password_nr)}")

    def read_all(self):
        rows = self.service.execute_command("SELECT * FROM password")
        print("\nNr\tTitle\tUsername\tPassword\n"
              "------------------------------------")
        for i in rows:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\n")

    def delete_data(self, password_nr):
        self.service.execute_command(f"DELETE FROM password WHERE password_nr ={str(password_nr)}")

    def close_database(self):
        self.connection.close()




