def generate_password():
    password_length = ask_length()
    password_writing = ask_password_writing()


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
