import argparse
from MasterPasswordController import MasterPasswordController
from PasswordController import PasswordController
from ClipboardService import ClipboardService
from GeneratePassword import GeneratePassword
import time
import hashlib
from getpass import getpass


class Command:

    def __init__(self):
        self.password_controller = PasswordController()
        self.master_password_controller = MasterPasswordController()
        self.clipboard = ClipboardService()
        self.password_generator = GeneratePassword()

    def last_login_check(self):

    # the time is stored in an integer
    # the current time is subtracted from the time of the last login
    # and the result (time_delta) is the seconds between the logins.

        time_now = int(time.time())
        time_last_login = self.master_password_controller.read_last_login()

        time_delta = time_now - time_last_login

    # check if it is more than 300 seconds (5min)

        if time_delta >= 300:
            return False
        else:
            return True

    def is_correct_master_password(self, i=0):

        if self.last_login_check():
            return True

        if i == 5:
            return False

        master_password_try = getpass("Login with your Master Password: ")

        #master_password_try = input("Login with your Master Password: ")
        master_password_try = hashlib.sha512(master_password_try.encode("utf-8")).hexdigest()

        if master_password_try == self.master_password_controller.read_master_password():
            self.master_password_controller.update_timestamp()
            return True
        else:
            print('Incorrect Master Password')
            i += 1
            return self.is_correct_master_password(i)

    def process(self):

    # all arugments are added
    # with 'choice' you set an input condition

        parser = argparse.ArgumentParser()
        parser.add_argument("operation", choices=["add", "delete", "copy", "update", "read"])
        parser.add_argument("-n", "-number", type=int)
        parser.add_argument("-t", "-title")
        parser.add_argument("-u", "-username")
        parser.add_argument("-p", "-password")
        parser.add_argument("-generatepassword", action="store_true")
        parser.add_argument("-m", "-master-password")
        args = parser.parse_args()

    # here all different possible inputs are checked with an if statement
    # If you write in illogical arguments, you will fall into the else case and get an error printed
    # For each possible case, the program jumps further into the PasswordController or
    # MasterpasswordContorller class, where the processing takes place.

    # for 'add' and 'update' the operation 'or' was used and then in the method
    # an if was used to see which of the two variables in the terminal was given as an argument.
    # this way the code can be shortened a little.

    # it asks for the master password every time you change it, but since you have 5 minutes of free access,
    # it only asks for it the first time you use it.

        if args.operation == "add" and args.t and args.u and (args.p or args.generatepassword):
            self.is_correct_master_password()
            if args.generatepassword:
                password = self.password_generator.generate_password()
            else:
                password = args.p

            self.password_controller.insert_data(args.t, args.u, password)
            print("The tuple insert to database")

        elif args.operation == "copy" and args.n:
            self.is_correct_master_password()
            number, title, username, password = self.password_controller.read_data(args.n)[0]
            print("Username: ", username, " | password copied to clipboard for the next 30 seconds")
            self.clipboard.copy_to_clipboard(password)

        elif args.operation == "read":
            self.is_correct_master_password()
            self.password_controller.read_all()

        elif args.operation == "delete" and args.n:
            self.is_correct_master_password()
            choose = input("Are you sure you want to delete the data?\n\n1 to delete\n2 to cancel: ")
            if choose == "1":
                self.password_controller.delete_data(args.n)
                print(f"The tuple {args.n} deleted")
            elif choose == "2":
                print("The process was canceled")
            else:
                print("Unknown decision")

        elif args.operation == "update" and args.m:
            self.is_correct_master_password()
            args.m = hashlib.sha512(args.m.encode("utf-8")).hexdigest()
            self.master_password_controller.update_master_password(args.m)
            print("The Master Password was changed successfully")

        elif args.operation == "update" and args.n and (args.p or args.u):
            self.is_correct_master_password()
            if args.p:
                self.password_controller.update_password(args.n, args.p)
            else:
                self.password_controller.update_username(args.n, args.u)
            print("The Password was changed successfully")

        else:
            print("ERROR")

    def all(self):

        self.master_password_controller.create_master_password_table()
        self.password_controller.create_password_table()

        try:
            # Master password exists, go in process method!
            self.process()
        except IndexError:
            # Ask the user tho create a master password
            # The password get hashed and insert in der master password table
            master_password = input("Choose Master Password: ")
            master_password = hashlib.sha512(master_password.encode("utf-8")).hexdigest()
            self.master_password_controller.insert_data(master_password)
            self.process()
