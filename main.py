import DatabaseConnector as db


def print_hi(name, alter):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ist {alter} Jahre alt')


def is_correct_master_password(i=0):
    if i == 5:
        return False

    master_password_try = input("Login with your Master Password: ")

    if master_password_try == master_password:
        return True
    else:
        print('Incorrect Master Password')
        i += 1
        return is_correct_master_password(i)


def new_password():
    title = input("\nWrite down the Title: ")
    username = input("Write down the Username: ")
    password = input("Write down the Password: ")
    db.insert_data(connection, title, username, password)


def delete_password():
    choose = input("Write the Title of the deleted Password")


def chance_master_password():
    new_master_password = input("\nChoose a new Master Password: ")


if __name__ == '__main__':

    connection = db.connect_to_db()
    db.create_table(connection)

    master_password = 'Key123'

    if is_correct_master_password():

        while True:

            print("Press 'A' for a New Password")
            print("Press 'B' to Delete a Password")
            print("Press 'C' to change the Master Password")
            print("Press 'D' to exit")
            print("Press 'E' to view all Data")

            decision = input("Choose your decision: ")

            if decision == "A":
                new_password()

            elif decision == "B":
                delete_password()

            elif decision == "C":
                chance_master_password()

            elif decision == "D":
                exit()

            elif decision == "E":
                if is_correct_master_password():
                    print(db.read_all(connection))

            else:
                print("Unknown decision")

        #print(db.read_data(connection, 1))
