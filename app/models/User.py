from bcrypt import checkpw, gensalt, hashpw


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def hash_password(self, password):
        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        confirmed = checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
        return confirmed
    
class LoginDTO:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class RegisterDTO:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password