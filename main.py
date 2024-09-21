class User:
    def __init__(self, id, name, access_level):
        self.id = id
        self.name = name
        self.access_level = access_level

    def user_id(self):
        return f' id пользователя {self.id}'

    def user_name(self):
        return f' имя пользователя {self.name}'

    def user_access_level(self):
        return f' уровень доступа пользователя {self.access_level}'


class Admin(User):
    def __init__(self, id, name, access_level, admin_level):
        super().__init__(id, name, access_level)
        self.__admin_level = admin_level

    def add_user(self):
        return f' добавлен новый пользователь id {self.id}, name {self.name}, access_level {self.access_level}'

    def remove_user(self, user_id):
        return f' удален пользователь с id {user_id}'

    def get_admin_level(self):
        return f'Уровень администратора: {self.__admin_level}'


user1 = User(1, 'Алексей', 'Стандартный')
admin1 = Admin(2, 'Мария', 'Администратор', 'Высокий')
user2 = User(3,'Иван', 'Стандартный')
admin2 = Admin(4,'Егор','Администратор','Высокий')

# Вызов методов класса User
print(user1.user_id())
print(user1.user_name())
print(user1.user_access_level())

print(user2.user_id())
print(user2.user_name())
print(user2.user_access_level())


# Вызов методов класса Admin
print(admin1.user_id())
print(admin1.user_name())
print(admin1.user_access_level())

print(admin2.user_id())
print(admin2.user_name())
print(admin2.user_access_level())


print(admin2.get_admin_level())
print(admin2.add_user())
print(admin1.remove_user(1))

