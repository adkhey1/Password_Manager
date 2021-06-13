from MasterPasswordController import MasterPasswordController
from PasswordController import PasswordController
from ClipboardService import ClipboardService
from GeneratePassword import GeneratePassword
import time
import os


class Main:

    def __init__(self):
        self.password_controller = PasswordController()
        self.master_password_controller = MasterPasswordController()
        self.clipboard = ClipboardService()
        self.password_generator = GeneratePassword()

    def last_login_check(self):

        time_now = int(time.time())
        time_last_login = self.master_password_controller.read_last_login()

        time_delta = time_now - time_last_login  # Time between now and last login in seconds

        if time_delta >= 300:
            return False
        else:
            return True

    def is_correct_master_password(self, i=0):

        if self.last_login_check():
            return True

        if i == 5:
            return False

        #master_password_try = getpass.getpass(prompt='Password: ', stream=None)

        master_password_try = input("Login with your Master Password: ")

        if master_password_try == self.master_password_controller.read_master_password():
            self.master_password_controller.update_timestamp()
            return True
        else:
            print('Incorrect Master Password')
            i += 1
            return self.is_correct_master_password(i)

    def new_password(self):
        title = input("\nWrite down the Title: ")
        username = input("Write down the Username: ")
        choice = input("1 to autogenerate password \n2 to write your own password: ")
        if choice == "2":
            password = input("Write down the Password: ")
            self.password_controller.insert_data(title, username, password)
            print("\nThe new Password is saved.")
        elif choice == "1":
            password = self.password_generator.generate_password()
            self.password_controller.insert_data(title, username, password)
            print("\nThe new Password is saved.")
        else:
            print("\nUnknown decision")

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
            self.action_menu()
        else:
            return print("Unknown decision\n"), self.delete_password()

    def chance_master_password(self):
        new_master_password = input("\nChoose a new Master Password: ")
        self.master_password_controller.update_master_password(new_master_password)

    def view_data(self):
        choose = input("\n1 to view all Data\n2 to view certain Data: ")
        if choose == "1":
            if self.is_correct_master_password():
                self.password_controller.read_all()
        elif choose == "2":
            password_nr = input("\nChoose your password number")
            number, title, username, password = self.password_controller.read_data(password_nr)[0]
            print("Username: ", username, " | password copied to clipboard for the next 30 seconds")
            self.clipboard.copy_to_clipboard(password)
            return self.action_menu()
        else:
            return print("\nUnknown decision")

    def change_data(self):
        choose = input("\n1 to change Password \n2 to change Username: ")
        if choose == "1":
            password_nr = input("Choose your password number: ")
            new_password = input("Choose the new Password: ")
            self.password_controller.update_password(password_nr, new_password)
        elif choose == "2":
            password_nr = input("Choose your password number: ")
            new_username = input("Choose the new Username: ")
            self.password_controller.update_username(password_nr, new_username)
        else:
            print("\nUnknown decision")


    def action_menu(self):

        while True:

            print("\n---------------------------------")
            print("Action Menu:\n")
            print("Press '1' for a New Password")
            print("Press '2' to Delete a Password")
            print("Press '3' to change the Master Password")
            print("Press '4' to view Data")
            print("Press '5' to change Data")
            print("Press '6' to exit")
            print("---------------------------------\n")

            decision = input("Choose your decision: ")

            if decision == "1":
                self.new_password()

            elif decision == "2":
                self.delete_password()

            elif decision == "3":
                self.chance_master_password()

            elif decision == "5":
                self.change_data()

            elif decision == "6":
                exit()

            elif decision == "4":
                self.view_data()

            else:
                print("Unknown decision")

    def all(self):

        print("Welcome to safe world\n")
        self.master_password_controller.create_master_password_table()
        self.password_controller.create_password_table()

        try:
            # Master password exists, ask user for it!
            self.is_correct_master_password()
        except IndexError:
            # Ask the user tho create a master password
            master_password = input("Choose Master Password: ")
            self.master_password_controller.insert_data(master_password)

        self.action_menu()

main = Main()

main.all()

