# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
# на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, id, name):
        self.__id = id
        self._name = name
        self.__access_level = 'user'
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__access_level = 'admin'

    def add_user(self, users, user):
        users.append(user)
        print(f'Пользователь c ID - {user.get_id()} и именем - {user.get_name()}, добавлен в систему')

    def remove_user(self, users, id):
        found = False
        for i, user in enumerate(users):
            if user.get_id() == id:
                del users[i]
                found = True
                print (f'Пользователь с ID - {id} удален из системы')
                break
        if not found:
            print(f'Пользователь с ID - {id} не найден в системе')
users = [
    User(1, 'Иван'),
    User(2, 'Анна'),
    User(3, 'Николай'),
    User(4, 'Евгений')
]

admin = Admin(5, 'Николай')

admin.add_user(users, User(6, 'Александр'))
admin.remove_user(users,3)
admin.remove_user(users, 66)




