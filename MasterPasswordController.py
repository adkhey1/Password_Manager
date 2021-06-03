from DatabaseService import DatabaseService
import datetime


class MasterPasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_master_password_table(self):
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, lastlogin DATE)""" and f"INSERT INTO Master_password "
                                                                      f"(master_password,lastlogin) VALUES (Key123,"
                                                                      f"{datetime.now()})")

    def read_data(self, master_password):
        self.service.execute_command(f"SELECT * FROM Master_password WHERE master_password = {master_password}")

    def update_master_password(self, master_password):
        self.service.execute_command("UPDATE Master_password SET master_password = ? WHERE master_password = ",
                                     str(master_password))

    def update_last_login(self, lli):
        self.service.execute_command("UPDATE Master_password SET lastlogin = ? WHERE lastlogin = lastlogin ",
                                     datetime.now())

    def close_database(self):
        self.connection.close()


