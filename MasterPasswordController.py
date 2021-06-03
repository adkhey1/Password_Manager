from DatabaseService import DatabaseService


class MasterPasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_password_table(self):
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, lastlogin DATE)""" and f"INSERT INTO Master_password "
                                                                      f"(master_password,lastlogin) VALUES (Key123,"
                                                                      f"{datetime.now()})")
