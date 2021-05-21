import sqlite3

connection = sqlite3.connect('Password_Database.db')

cursor = connection.cursor()

table1 = '''Create a Table if none exist
  password(password_nr INTEGER PRIMARY KEY, title TEXT, username TEXT, password TEXT )'''

cursor.execute(table1)


        print("Press 'A' for a New Password")
        print("Press 'B' to Delete a Password")
        print("Press 'C' to change the Master Password\n")

        decision = input("Choose your decision: ")

        if decision == "A":

            title = input("\nWrite down the Title: ")
            username = input("Write down the Username: ")
            password = input("Write down the Password: ")

            #hier nochmal eine abfrage ob man wirklich das neue Passwort anlegen möchte

            cursor.execute("INSERT INTO password VALUES" + title + username + password)

        elif decision == "B":

            choose = input("Write the Title of the deleted Password")

            cursor.execute("DELETE FROM password WHERE choose ")

        elif decision == "C":

choose = input("Tip the new Master Key: ")

cursor.execute("UPDATE password SET" + choose )

        else:
           print("Unknown decision")









def print_hi(name, alter):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ist {alter} Jahre alt')



if __name__ == '__main__':


    print_hi('PyCharm', '17')

    master_Password_Try = input("Login with your Master Password: ")

    if Master_Password == master_Password_Try:

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

