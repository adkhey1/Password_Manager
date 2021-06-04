from DatabaseService import DatabaseService


class MasterPasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_master_password_table(self):
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, timestamp TIMESTAMP)""")

    def insert_data(self):
        self.service.execute_command("INSERT INTO Master_password (master_password,timestamp) VALUES ('Key123',"
                                     "CURRENT_TIMESTAMP)")

    def read_master_password(self):
        return self.service.execute_command("SELECT master_password FROM Master_password")[0][0]

    def update_master_password(self, master_password):
        self.service.execute_command("UPDATE Master_password SET master_password = ? WHERE master_password = ",
                                     str(master_password))

    def update_timestamp(self):
        self.service.execute_command("UPDATE Master_password SET timestamp = CURRENT_TIMESTAMP"
                                     " WHERE timestamp = timestamp")

    def close_database(self):
        self.connection.close()


