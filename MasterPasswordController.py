import time
from DatabaseService import DatabaseService


class MasterPasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_master_password_table(self):
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, last_login INTEGER)""")

    def insert_data(self, master_password):
        self.service.execute_command(f"INSERT INTO Master_password (master_password, last_login) VALUES (?,?)",
                                     (master_password, int(time.time())))

    def read_master_password(self):
        return self.service.execute_command("SELECT master_password FROM Master_password")[0][0]

    def read_last_login(self):
        return self.service.execute_command("SELECT last_login FROM Master_password")[0][0]

    def update_master_password(self, master_password):
        self.service.execute_command("UPDATE Master_password SET master_password = ? WHERE master_password = 'Key123'", (str(master_password), ))

    def update_timestamp(self):
        self.service.execute_command("UPDATE Master_password SET last_login = ?", (int(time.time()), ))

    def close_database(self):
        self.connection.close()
