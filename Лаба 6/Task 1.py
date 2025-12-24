class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно изменён")

    def check_password(self, password):
        return self.__password == password
    
user = UserAccount("Igor", "pondyakov777@mail.ru","oldest2424")
print(user.check_password("oldest2424"))
user.set_password("new2424")
print(user.check_password("new2424"))
print(user.check_password("aderdemerede"))