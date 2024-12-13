class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password



user = UserAccount(username="egor", email="egorgutnik17@gmail.com", password="12345678")

print(user.check_password("initial_password"))

user.set_password("new_secure_password")

print(user.check_password("new_secure_password"))
print(user.check_password("initial_password"))