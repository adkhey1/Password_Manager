import random
import string


class GeneratePassword:

    def generate_password(self):
        password_length = self.ask_length()
        password_writing = self.ask_password_writing()
        password_symblos = self.symbols()
        password_digit = self.digit()

        self.create_password(password_length, password_writing, password_symblos, password_digit)

    def ask_length(self):
        password_length = input('Wie lang soll dein Passwort sein?: ')
        try:
            password_length = int(password_length)
            if password_length >= 8:
                return password_length
            else:
                print("Please enter an integer higher than 8")
                return self.ask_length()
        except ValueError:
            # Handle the exception
            print('Please enter an integer')
            return self.ask_length()

    def ask_password_writing(self):
        password_writing = input('Wie soll ihr Passswort aussehen?\nGroßschreibung(1)\nKleinschreibung(2)'
                                 '\nGroß- und kleinschreibung(3)')
        try:
            password_writing = int(password_writing)
            if 0 < password_writing <= 3:
                return password_writing
            else:
                self.ask_password_writing()
        except ValueError:
            # Handle the exception
            print('Please enter an integer between 1 and 3')
            return self.ask_password_writing()

    def symbols(self):
        password_symblos = input('Soll ihr Password Sonderzeichen haben\n(1) Ja\n(2) Nein')

        try:
            password_symblos = int(password_symblos)
            if 0 < password_symblos <= 2:
                return password_symblos
            else:
                self.symbols()
        except ValueError:
            # Handle the exception
            print('Please enter an integer 1 or 2')
            return self.symbols()

    def digit(self):
        password_digit = input('Soll ihr Password Zahlen haben\n(1) Ja\n(2) Nein')

        try:
            password_digit = int(password_digit)
            if 0 < password_digit <= 2:
                return password_digit
            else:
                self.digit()
        except ValueError:
            # Handle the exception
            print('Please enter an integer 1 or 2')
            return self.digit()

    def create_password(self, password_length, password_writing, password_symblos, password_digit):

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
        elif password_writing == 2 and password_symblos == 2 and password_digit == 2:
            choose = lower
        elif password_writing == 1 and password_symblos == 2 and password_digit == 2:
            choose = upper
        elif password_writing == 3 and password_symblos == 2 and password_digit == 2:
            choose = upper + lower

        temp = random.sample(choose, length)

        password = "".join(temp)

        print(password)


main = GeneratePassword()

main.generate_password()
