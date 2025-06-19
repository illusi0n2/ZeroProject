# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
#
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
#
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
#
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
#
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять,
# не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    def __init__(self, weapon_name):
        self.weapon_name = weapon_name

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

# Шаг 2: Реализуйте конкретные типы оружия
class Bow(Weapon):
    def attack(self):
        print("Боец выстрелил из лука")

# Шаг 3: Модифицируйте класс Fighter
class Fighter():
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        print(f'Боец выбирает {weapon.weapon_name}')
        self.weapon = weapon

class Monster(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def die(self):
        pass

class Goblin(Monster):
    def __init__(self, name = 'Гоблин'):
        super().__init__(name)

    def attack(self):
        print(f'{self.name} атакует')

    def die(self):
        print(f'{self.name} умирает')

sword = Sword('меч')
bow = Bow('лук')
fighter_Ivan = Fighter('Иван', sword)
goblin = Goblin()

# Шаг 4: Реализация боя
def fight(fighter, monster):
    while True:  # Бесконечный цикл для продолжения игры
        choice = input('Выбери действие (1 - выбрать оружие, 2 - атаковать, 3 - завершить бой): ')
        if choice == '1':
            while True:
                choice = input('Какое оружие выбрать (1 - меч, 2 - лук): ')
                if choice == '1':
                    fighter.change_weapon(sword)
                    break
                elif choice == '2':
                    fighter.change_weapon(bow)
                    break
                else:
                    print('Необходимо ввести значение 1 или 2')
        elif choice == '2':
            fighter.weapon.attack()
            monster.die()
        elif choice == '3':
            break
        else:
            print('Необходимо ввести значение 1, 2 или 3')

fight(fighter_Ivan, goblin)