# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name, alter):
    # Use a breakpoint in the code line below to debug your script.o


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm', '17')

    Master_Password = 'Key123'

    master_Password_Try = input("Login with your Master Password: ")

    if Master_Password == master_Password_Try:

        print("Press '1' for a New Password")
        print("Press '2' to Delete a Password")
        print("Press '3' to change the Master Password\n")

        decision = input("Choose your decision: ")

        if decision == "1":

            title = input("\nWrite down the Title: ")
            username = input("Write down the Username: ")
            password = input("Write down the Password: ")

        elif decision == "2":

            choose = input("Write the Title of the deleted Password")
        elif decision == "3":

            new_master_password = input("\nChoose a new Master Password: ")
        else:
            print("Unknown decision")


if Master_Password !=master_Password_Try:
        master_Password_Try = input("Login with your Master Password: ")

asdsadsadsadsadsadsadxycsycsdasd




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
