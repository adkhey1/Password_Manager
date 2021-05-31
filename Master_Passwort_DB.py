import sqlite3
import datetime


def connect_to_db():
    connection2 = sqlite3.connect("Master_Password_Database.db")
    return connection2


def create_table(connection2):
    cursor = connection2.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
      Master_password(master_password VARCHAR, lastlogin DATE)""")
    cursor.execute(f"INSERT INTO Master_password (master_password,lastlogin) VALUES (Key123,{datetime.now()})")


def read_data(connection2, master_password):
    cursor = connection2.cursor()
    cursor.execute("SELECT * FROM Master_password WHERE master_password = ?", str(master_password))
    return cursor.fetchall()


def update_master_password(connection2, master_password):
    cursor = connection2.cursor()
    cursor.execute("UPDATE Master_password SET master_password = ? WHERE master_password = Key123", str(master_password))


def update_lastlogin(connection2):
    cursor = connection2.cursor()
    cursor.execute("UPDATE Master_password SET lastlogin = ? WHERE lastlogin = lastlogin ", datetime.now())


def close_db_connection(connection2):
    connection2.close()
