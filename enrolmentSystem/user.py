import re

class User:
    def __init__(self, name, email, password):
        print(name)
        if not self.is_email_valid(email):
            raise ValueError("Invalid email. Email must end with @university.com")
        if not self.is_password_valid(password):
            raise ValueError("Invalid password. Password must start with an uppercase letter, have at least 5 letters, and be followed by 3 or more digits.")

        self.name = name
        self.email = email
        self.password = password
        self.is_logged_in = False

    @staticmethod
    def is_email_valid(email):
        # Validate the email to ensure it ends with @university.com
        return re.match(r"^[a-zA-Z0-9._%+-]+@university\.com$", email) is not None

    @staticmethod
    def is_password_valid(password):
        # Validate the password: Starts with uppercase, followed by at least 5 letters, then 3+ digits
        return re.match(r"^[A-Z][a-zA-Z]{4,}[0-9]{3,}$", password) is not None

    def login(self, password):
        if self.password == password:
            self.is_logged_in = True
            print(f"{self.name} logged in successfully.")
            return True
        else:
            print("Invalid password.")
            return False

    def logout(self):
        self.is_logged_in = False
        print(f"{self.name} logged out.")
