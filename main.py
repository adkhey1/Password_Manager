# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name, alter):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ist {alter} Jahre alt')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm', '17')

    Master_Password = 'Key123'

    master_Password_Try = input("Login with your Master Password: ")

    if Master_Password == master_Password_Try:

        print("Press 'A' for a New Password")
        print("Press 'B' to Delete a Password")
        print("Press 'C' to change the Master Password\n")

pdi

        decision = input("Choose your decision: ")

        if decision == "A":

            title = input("\nWrite down the Title: ")
            username = input("Write down the Username: ")
            password = input("Write down the Password: ")

        elif decision == "B":

            choose = input("Write the Title of the deleted Password")
        elif decision == "C":

            new_master_password = input("\nChoose a new Master Password: ")
        else:
            print("Unknown decision")



    else:
        master_Password_Try = input("Login with your Master Password: ")











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
