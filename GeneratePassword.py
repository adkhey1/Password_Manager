import random
import string


class GeneratePassword:

    def generate_password(self):
        # creates a separate method for each condition
        password_length = self.ask_length()
        password_writing = self.ask_password_writing()
        password_symbols = self.symbols()
        password_digit = self.digit()

        return self.create_password(password_length, password_writing, password_symbols, password_digit)

    def ask_length(self):
        # checks if it has more than 8 letters, if yes he sends it back, if no he ask again
        password_length = input('How long should your password be?: ')
        try:
            password_length = int(password_length)
            if password_length >= 8:
                return password_length
            else:
                print('Please enter an integer more than 8\n')
                return self.ask_length()
        except ValueError:
            # Handle the exception
            print('Please enter an integer')
            return self.ask_length()

    def ask_password_writing(self):
        # choose how you want the password to be written and than you send it back again
        # catching incorrect inputs with try catch
        password_writing = input('\nWhat should your password look like?\n(1) Upper case\n(2) Lower case'
                                 '\n(3) Upper- and lower case')
        try:
            password_writing = int(password_writing)
            if 0 < password_writing <= 3:
                return password_writing
            else:
                print('Please enter an integer between 1 and 3\n')
                return self.ask_password_writing()
        except ValueError:
            # Handle the exception
            print('Please enter an integer between 1 and 3')
            return self.ask_password_writing()

    def symbols(self):
        # choose how you want the password to be written and than you send it back again
        # catching incorrect inputs with try catch
        password_symbols = input('Should your password have special characters\n(1) Yes\n(2) No')

        try:
            password_symbols = int(password_symbols)
            if 0 < password_symbols <= 2:
                return password_symbols
            else:
                print('Please enter an integer between 1 and 2\n')
                return self.symbols()
        except ValueError:
            # Handle the exception
            print('Please enter an integer 1 or 2')
            return self.symbols()

    def digit(self):
        # choose how you want the password to be written and than you send it back again
        # catching incorrect inputs with try catch
        password_digit = input('Should your password have number\n(1) Yes\n(2) No')

        try:
            password_digit = int(password_digit)
            if 0 < password_digit <= 2:
                return password_digit
            else:
                print('Please enter an integer between 1 and 3\n')
                return self.digit()
        except ValueError:
            # Handle the exception
            print('Please enter an integer 1 or 2')
            return self.digit()

    def create_password(self, password_length, password_writing, password_symbols, password_digit):
        # goes through all options and bills the desired password with the variable choose
        length = password_length
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        num = string.digits
        symbols = string.punctuation

        if password_writing == 1 and password_symbols == 1 and password_digit == 1:
            choose = upper + num + symbols
        elif password_writing == 2 and password_symbols == 1 and password_digit == 1:
            choose = lower + num + symbols
        elif password_writing == 3 and password_symbols == 1 and password_digit == 1:
            choose = upper + lower + num + symbols
        elif password_writing == 1 and password_symbols == 2 and password_digit == 1:
            choose = upper + symbols
        elif password_writing == 2 and password_symbols == 2 and password_digit == 1:
            choose = lower + symbols
        elif password_writing == 3 and password_symbols == 2 and password_digit == 1:
            choose = upper + lower + symbols
        elif password_writing == 1 and password_symbols == 1 and password_digit == 2:
            choose = upper + num
        elif password_writing == 2 and password_symbols == 1 and password_digit == 2:
            choose = lower + num
        elif password_writing == 3 and password_symbols == 1 and password_digit == 2:
            choose = upper + lower + num
        elif password_writing == 1 and password_symbols == 2 and password_digit == 2:
            choose = upper
        elif password_writing == 2 and password_symbols == 2 and password_digit == 2:
            choose = lower
        elif password_writing == 3 and password_symbols == 2 and password_digit == 2:
            choose = upper + lower
        # creates an empty String and adds the selection with the length and return it
        return "".join(random.sample(choose, length))

