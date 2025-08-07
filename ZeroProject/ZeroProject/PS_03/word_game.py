import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    translator = Translator()
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Переводим слово на русский язык
        russian_word = translator.translate(english_word, dest='ru').text
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Переводим описание на русский язык
        word_definition_ru = translator.translate(word_definition, dest='ru').text
        # Чтобы программа возвращала словарь
        return {
            "word": russian_word,
            "word_definition": word_definition_ru,
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("word")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()