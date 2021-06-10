import time
from DatabaseService import DatabaseService


class MasterPasswordController:

    def __init__(self):
        # connect to the DatabaseService class (generator)
        self.service = DatabaseService()

    def create_master_password_table(self):
        # create Table with the columns master password and last login (if not exist)
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, last_login INTEGER)""")

    def insert_data(self, master_password):
        # adds the selected password and time at the beginning of the program
        # then it never called out again (only the values are changed, nothing new is added)
        self.service.execute_command(f"INSERT INTO Master_password (master_password, last_login) VALUES (?,?)",
                                     (master_password, int(time.time())))

    def read_master_password(self):
        # read the master password (we need this for the login request)
        return self.service.execute_command("SELECT master_password FROM Master_password")[0][0]

    def read_last_login(self):
        # read last login time (we need this to see how long it has been since the last login)
        return self.service.execute_command("SELECT last_login FROM Master_password")[0][0]

    def update_master_password(self, master_password):
        # update the master password
        self.service.execute_command("UPDATE Master_password SET master_password = ? ", (str(master_password), ))

    def update_timestamp(self):
        # update the last login whenever we have a successfully logged in with the master password
        self.service.execute_command("UPDATE Master_password SET last_login = ?", (int(time.time()), ))

    def close_database(self):
        # close the database
        self.connection.close()
