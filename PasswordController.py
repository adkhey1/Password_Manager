from DatabaseService import DatabaseService


class PasswordController:

    def __init__(self):
        self.service = DatabaseService()

    def create_password_table(self):
        # create Table with the columns password nr, title, username and password (if not exist)
        self.service.execute_command("""CREATE TABLE IF NOT EXISTS
      password(password_nr INTEGER PRIMARY KEY , title VARCHAR, username VARCHAR, password VARCHAR)""")

    def insert_data(self, title, username, password):
        # insert new tuples with title, username and password
        # the password number is created automatically in ascending order
        self.service.execute_command(f"INSERT INTO password (title, username, password) VALUES (?, ?, ?)",
                                     (title, username, password))

    def read_data(self, password_nr):
        # reads a specific tuple that you specify in the console with the password number
        return self.service.execute_command(f"SELECT * FROM password WHERE password_nr = {str(password_nr)}")

    def read_all(self):
        # read all tuples and print all out on the console
        rows = self.service.execute_command("SELECT * FROM password")
        print("\nNr\tTitle\tUsername\tPassword\n"
              "------------------------------------")
        for i in rows:
            print(i[0], "\t", i[1], "\t", i[2], "\t", "*****", "\n")

    def delete_data(self, password_nr):
        # delete a specific tuple that you specify in the console with the password number
        self.service.execute_command(f"DELETE FROM password WHERE password_nr ={str(password_nr)}")

    def close_database(self):
        # close connection to the data base
        self.connection.close()




