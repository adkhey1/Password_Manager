import DatabaseConnector as db


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
    print("\nThe new Password is saved.")


def delete_password():
    choose = input("Write the PasswordNr of the deleted Password: ")
    delete_decision = input("\n---------------------------------"
                            "\nAre you sure you want to delete the data?\n\n1 to delete\n2 to cancel"
                            "\n3 to go back to the Action Menu\n---------------------------------"
                            "\n\nChoose your decision: ")
    if delete_decision == "1":
        db.delete_data_nr(connection, choose)
        print("\nThe Password Number: ", choose, " has been deleted.")
    elif delete_decision == "2":
        return delete_password()
    elif delete_decision == "3":
        return True
    else:
        return print("Unknown decision\n"), delete_password()


def chance_master_password():
    new_master_password = input("\nChoose a new Master Password: ")


if __name__ == '__main__':

    connection = db.connect_to_db()
    db.create_table(connection)

    master_password = 'Key123'

    print("Welcome to safe word\n")
    if is_correct_master_password():

        while True:

            print("\n---------------------------------")
            print("Action Menu:\n")
            print("Press '1' for a New Password")
            print("Press '2' to Delete a Password")
            print("Press '3' to change the Master Password")
            print("Press '4' to view all Data")
            print("Press '5' to exit")
            print("---------------------------------\n")

            decision = input("Choose your decision: ")

            if decision == "1":
                new_password()

            elif decision == "2":
                delete_password()

            elif decision == "3":
                chance_master_password()

            elif decision == "5":
                exit()

            elif decision == "4":
                if is_correct_master_password():
                    print(db.read_all(connection))

            else:
                print("Unknown decision")

        #print(db.read_data(connection, 1))
