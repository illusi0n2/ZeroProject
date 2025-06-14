# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import json
from pathlib import Path

#Реализация пунктов 1 и 2 из постановки задачи
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f'{self.name} издает звук'

    def eat(self):
        print(f'{self.name} кушает')

    def __str__(self):
        return f'\n{self.name} возраст, которого(ой) - {self.age}'

    def __repr__(self):
        return self.__str__()

    def __dict__(self):
        return {
            "__class__": "Animal",
            "name": self.name,
            "age": self.age
        }

class Bird(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def make_sound(self):
        return f'Птица{self.name} села на дерево и издает звук {self.sound}'

    def __dict__(self):
        return {
            "__class__": "Bird",
            "name": self.name,
            "age": self.age,
            "sound": self.sound
        }

class Mammal(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def make_sound(self):
        return f'Млекопитающее {self.name} лежит на земле и издает звук {self.sound}'

    def __dict__(self):
        return {
            "__class__": "Mammal",
            "name": self.name,
            "age": self.age,
            "sound": self.sound
        }

class Reptile(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def make_sound(self):
        return f'Рептилия {self.name} залезла под камень и издает звук {self.sound}'

    def __dict__(self):
        return {
            "__class__": "Reptile",
            "name": self.name,
            "age": self.age,
            "sound": self.sound
        }

#Выполнение пункта 3 - "Продемонстрируйте полиморфизм"
animals_list = [
    Bird('Воробей', 2, 'чирик'),
    Mammal('Волк', 5, 'рррр'),
    Reptile('Змея', 5, 'сссс')
]
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals_list)

#Реализация пункта 4 из постановки задачи - Используйте композицию для создания класса `Zoo`
class Zoo():
    def __init__(self, name_zoo, animals, staff):
        assert isinstance(animals, list), "Необходимо передать список животных в зоопарке"
        assert isinstance(staff, list), "Необходимо передать список сотрудников зоопарка"
        self.name_zoo = name_zoo
        self.animals = animals
        self.staff = staff

    def add_animal(self, animal):
        assert isinstance(animal, Animal), "Необходимо передавать класс животных(Animal) либо его наследников"
        self.animals.append(animal)

    def add_employee(self, employee):
        assert isinstance(employee, Staff), "Необходимо передавать класс персонала(Staff) либо его наследников"
        self.staff.append(employee)

    def get_all_animal(self):
        return self.animals
    def get_all_staff(self):
        return self.staff

    def save(self):
        # Создаем словарь для сериализации
        zoo_data = {
            "name_zoo": self.name_zoo,
            "animals": [animal.__dict__() for animal in self.animals],
            "staff": [employee.__dict__() for employee in self.staff]
        }

        # Сохраняем в файл
        with Path("zoo_data.json").open("w", encoding="utf-8") as file:
            json.dump(zoo_data, file, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls):
        try:
            with Path("zoo_data.json").open("r", encoding="utf-8") as file:
                zoo_data = json.load(file)

            # Создаем зоопарк с загруженными данными
            zoo = cls(zoo_data["name_zoo"], [], [])

            # Восстанавливаем животных
            for animal_data in zoo_data["animals"]:
                if animal_data["__class__"] == "Bird":
                    zoo.add_animal(Bird(
                        animal_data["name"],
                        animal_data["age"],
                        animal_data["sound"]
                    ))
                elif animal_data["__class__"] == "Mammal":
                    zoo.add_animal(Mammal(
                        animal_data["name"],
                        animal_data["age"],
                        animal_data["sound"]
                    ))
                elif animal_data["__class__"] == "Reptile":
                    zoo.add_animal(Reptile(
                        animal_data["name"],
                        animal_data["age"],
                        animal_data["sound"]
                    ))

            # Восстанавливаем сотрудников
            for employee_data in zoo_data["staff"]:
                if employee_data["__class__"] == "ZooKeeper":
                    zoo.add_employee(ZooKeeper(
                        employee_data["name"],
                    ))
                elif employee_data["__class__"] == "Veterinarian":
                    zoo.add_employee(Veterinarian(
                        employee_data["name"],
                    ))
                # Аналогично для других типов сотрудников

            return zoo
        except FileNotFoundError:
            print("Файл с данными зоопарка не найден")
            return None

#Выполнение пункта 5 - Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`
class Staff():
    def __init__(self, name, post = 'Разнорабочий'):
        self.name = name
        self.post = post

    def doing_job(self):
        return f'{self.name} делает какую-то работу'

    def __str__(self):
        return f'\n{self.name} занимает должность - {self.post}'

    def __repr__(self):
        return self.__str__()

    def __dict__(self):
        return {
            "__class__": "Staff",
            "name": self.name,
        }

class ZooKeeper(Staff):
    def __init__(self, name, post = 'Смотритель зоопарка'):
        super().__init__(name, post)
    def doing_job(self):
        return f'{self.name} покормил животных'

    def __dict__(self):
        return {
            "__class__": "ZooKeeper",
            "name": self.name,
        }

class Veterinarian(Staff):
    def __init__(self, name, post = 'Ветеринар'):
        super().__init__(name, post)

    def doing_job(self):
        return f'{self.name} проверил здоровье животных и занялся лечением заболевших'

    def __dict__(self):
        return {
            "__class__": "Veterinarian",
            "name": self.name,
        }

staff = [
    Staff('Николай'),
    ZooKeeper('Иван'),
    Veterinarian('Ирина')
]
zoo = Zoo('Новый зоопарк', animals_list, staff)
zoo.add_animal(Reptile('12431', 4, 'fdsfsdgsdgg'))
zoo.add_animal(Bird('Голубь', 5, 'курлык'))
zoo.add_employee(ZooKeeper('Семен'))
print(zoo.get_all_staff())
print(zoo.get_all_animal())
print(zoo.get_all_staff()[1].doing_job())

zoo.save() #Сохраняем состояние зоопарка в JSON zoo_data

loaded_zoo = Zoo.load() #Создаем новый зоопарк из ранее сохраненного файла с состоянием на момент сохранения