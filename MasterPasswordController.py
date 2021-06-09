from DatabaseService import DatabaseService


class MasterPasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_master_password_table(self):
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, login TIMESTAMP)""")

    def insert_data(self):
        self.service.execute_command("INSERT INTO Master_password (master_password,login) VALUES ('Key123',"
                                     "CURRENT_TIMESTAMP)")

    def read_master_password(self):
        return self.service.execute_command("SELECT master_password FROM Master_password")[0][0]

    def read_master_login(self):
        return self.service.execute_command("SELECT login FROM Master_password")[0][0]

    def update_master_password(self, master_password):
        self.service.execute_command("UPDATE Master_password SET master_password = ?", str(master_password))

    def update_timestamp(self):
        self.service.execute_command("UPDATE Master_password SET login = CURRENT_TIMESTAMP")

    def close_database(self):
        self.connection.close()


