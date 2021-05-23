import DatabaseConnector as db


def print_hi(name, alter):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ist {alter} Jahre alt')


if __name__ == '__main__':

    print_hi('PyCharm', '17')

    connection = db.connect_to_db()
    db.create_table(connection)
    db.insert_data(connection, 'test1', 'test2', 'test3')
    print(db.read_data(connection, 1))

    master_password = 'Key123'

    master_Password_Try = input("Login with your Master Password: ")

    if master_password == master_Password_Try:

        print("Press 'A' for a New Password")
        print("Press 'B' to Delete a Password")
        print("Press 'C' to change the Master Password\n")


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
