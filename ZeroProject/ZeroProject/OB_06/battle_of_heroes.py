# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по этапам/
# или создать kanban доску для работы над данным проектом

# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.

# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.

import random
import time
from abc import ABC, abstractmethod

#Создан абстрактный класс для возможности в будущем расширить классы героев
class Fighter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass

#Создан класс Героя
class Hero(Fighter):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        if other.health > 0:
            print(f'{self.name} атаковал {other.name} на {self.attack_power}. У бойца {other.name} осталось {other.health} жизней')
        else:
            print(f'{self.name} атаковал {other.name} на {self.attack_power}. Боец {other.name} побежден')

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

#Создан класс игры
class Game():
    def __init__(self, player: Fighter, computer: Fighter):
        self.player = player
        self.computer = computer

    def start(self):
        order = random.randint(1, 2) #Жеребьевка для выбора того, кто наносит первый удар
        if order == 1:
            while True:
                self.player.attack(self.computer)
                if not self.computer.is_alive(): #Проверяем остались ли жизни у противника
                    print(f'Победитель {self.player.name}')
                    break
                time.sleep(1)
                self.computer.attack(self.player)
                if not self.player.is_alive(): #Проверяем остались ли жизни у противника
                    print(f'Победитель {self.computer.name}')
                    break
                time.sleep(1)
        elif order == 2:
            while True:
                self.computer.attack(self.player)
                if not self.player.is_alive(): #Проверяем остались ли жизни у противника
                    print(f'Победитель {self.computer.name}')
                    break
                time.sleep(1)
                self.player.attack(self.computer)
                if not self.computer.is_alive(): #Проверяем остались ли жизни у противника
                    print(f'Победитель {self.player.name}')
                    break
                time.sleep(1)


player = Hero('Игрок')
comp = Hero('Компьютер')

game = Game(player, comp)
game.start()