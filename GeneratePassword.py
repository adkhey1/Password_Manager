import random
import string


def generate_password():
    password_length = ask_length()
    password_writing = ask_password_writing()
    password_symblos = symbols()
    password_digit = digit()

    create_password(password_length, password_writing, password_symblos, password_digit)


def ask_length():
    password_length = input('Wie lang soll dein Passwort sein?: ')
    try:
        password_length = int(password_length)
        return password_length
    except ValueError:
        # Handle the exception
        print('Please enter an integer')
        return ask_length()


def ask_password_writing():
    password_writing = input('Wie soll ihr Passswort aussehen?\nGroßschreibung(1)\nKleinschreibung(2)'
                             '\nGroß- und kleinschreibung(3)')
    try:
        password_writing = int(password_writing)
        if 0 < password_writing <= 3:
            return password_writing
        else:
            ask_password_writing()
    except ValueError:
        # Handle the exception
        print('Please enter an integer between 1 and 3')
        return ask_password_writing()


def symbols():
    password_symblos = input('Soll ihr Password Sonderzeichen haben\n(1) Ja\n(2) Nein')

    try:
        password_symblos = int(password_symblos)
        if 0 < password_symblos <= 2:
            return password_symblos
        else:
            symbols()
    except ValueError:
        # Handle the exception
        print('Please enter an integer 1 or 2')
        return symbols()


def digit():
    password_digit = input('Soll ihr Password Zahlen haben\n(1) Ja\n(2) Nein')

    try:
        password_digit = int(password_digit)
        if 0 < password_digit <= 2:
            return password_digit
        else:
            digit()
    except ValueError:
        # Handle the exception
        print('Please enter an integer 1 or 2')
        return digit()


def create_password(password_length, password_writing, password_symblos, password_digit):

    length = password_length
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    num = string.digits
    symbols = string.punctuation

    if password_writing == 1 and password_symblos == 1 and password_digit == 1:
        choose = upper + num + symbols
    elif password_writing == 2 and password_symblos == 1 and password_digit == 1:
        choose = lower + num + symbols
    elif password_writing == 3 and password_symblos == 1 and password_digit == 1:
        choose = upper + lower + num + symbols
    elif password_writing == 1 and password_symblos == 2 and password_digit == 1:
        choose = upper + symbols
    elif password_writing == 2 and password_symblos == 2 and password_digit == 1:
        choose = lower + symbols
    elif password_writing == 3 and password_symblos == 2 and password_digit == 1:
        choose = upper + lower + symbols
    elif password_writing == 1 and password_symblos == 1 and password_digit == 2:
        choose = upper + num
    elif password_writing == 2 and password_symblos == 1 and password_digit == 2:
        choose = lower + num
    elif password_writing == 3 and password_symblos == 1 and password_digit == 2:
        choose = upper + lower + num

    temp = random.sample(choose, length)

    password = "".join(temp)

    print(password)

