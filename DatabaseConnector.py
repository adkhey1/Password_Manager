import sqlite3


def connect_to_db():
    connection = sqlite3.connect("Password_Database.db")
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
      password(password_nr INTEGER PRIMARY KEY , title VARCHAR, username VARCHAR, password VARCHAR)""")


def insert_data(connection, title, username, password):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO password (title, username, password) VALUES (?, ?, ?)", (title, username, password))
    connection.commit()


def read_data(connection, password_nr):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM password WHERE password_nr = ?", str(password_nr))

    return cursor.fetchall()


def read_all(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM password")

    return cursor.fetchall()


def delete_data_nr(connection, password_nr):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM password WHERE password_nr =?", str(password_nr))
    connection.commit()


def close_db_connection(connection):
    connection.close()
