from MasterPasswordController import MasterPasswordController
from PasswordController import PasswordController


class Main:

    def __init__(self):
        self.password_controller = PasswordController()
        self.master_password_controller = MasterPasswordController()

    def is_correct_master_password(self, i=0):
        if i == 5:
            return False

        master_password_try = input("Login with your Master Password: ")

        if master_password_try == 'Key123':
            return True
        else:
            print('Incorrect Master Password')
            i += 1
            return self.is_correct_master_password(i)

    def new_password(self):
        title = input("\nWrite down the Title: ")
        username = input("Write down the Username: ")
        password = input("Write down the Password: ")
        self.password_controller.insert_data(title, username, password)
        print("\nThe new Password is saved.")

    def delete_password(self):
        choose = input("Write the PasswordNr of the deleted Password: ")
        delete_decision = input("\n---------------------------------"
                                "\nAre you sure you want to delete the data?\n\n1 to delete\n2 to cancel"
                                "\n3 to go back to the Action Menu\n---------------------------------"
                                "\n\nChoose your decision: ")
        if delete_decision == "1":
            self.password_controller.delete_data(choose)
            print("\nThe Password Number: ", choose, " has been deleted.")
        elif delete_decision == "2":
            return self.delete_password()
        elif delete_decision == "3":
            return True
        else:
            return print("Unknown decision\n"), self.delete_password()

    def chance_master_password(self):
        new_master_password = input("\nChoose a new Master Password: ")
        self.masterpassword_controller.update_master_password(self, new_master_password)

    def view_data(self):
        choose = input("\n1 to view all Data\n2 to view certain Data")
        if choose == "1":
            if self.is_correct_master_password():
                print(self.password_controller.read_all())
        elif choose == "2":
            password_nr = input("\nChoose your password number")
            self.password_controller.read_data(password_nr)

    def all(self):
        self.password_controller.create_password_table()
        self.master_password_controller.create_master_password_table()

        print("Welcome to safe word\n")

        if self.is_correct_master_password():

            while True:

                print("\n---------------------------------")
                print("Action Menu:\n")
                print("Press '1' for a New Password")
                print("Press '2' to Delete a Password")
                print("Press '3' to change the Master Password")
                print("Press '4' to view Data")
                print("Press '5' to exit")
                print("---------------------------------\n")

                decision = input("Choose your decision: ")

                if decision == "1":
                    self.new_password()

                elif decision == "2":
                    self.delete_password()

                elif decision == "3":
                    self.chance_master_password()

                elif decision == "5":
                    exit()

                elif decision == "4":
                    self.view_data()
                    if self.is_correct_master_password():
                        print(self.password_controller.read_all())

                else:
                    print("Unknown decision")

            # print(self.password_controller.read_data(1))


main = Main()
main.all()