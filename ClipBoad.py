import pyperclip as pc
import PasswordController

x =     def read_data(self, password_nr):
        self.service.execute_command(f"SELECT * FROM password WHERE password_nr = {str(password_nr)}", )


pc.copy(x)
a = pc.paste()
print(a)