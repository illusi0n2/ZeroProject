# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
#
# 1. Спрашивать у пользователя первоначальный запрос.
#
# 2. Переходить по первоначальному запросу в Википедии.
#
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
#     - листать параграфы статьи;
#     - перейти на одну из внутренних статей.
# выйти из программы.

import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.get('https://www.wikipedia.org/')

start_search_field = browser.find_element(By.XPATH, "//input [@id= 'searchInput']")
question = input('Введите свой запрос\n')
start_search_field.send_keys(question)
start_search_field.send_keys(Keys.RETURN)

#Метод для чтения параграфов на странице
def read_paragrafs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

#Метод для перехода по рандомной ссылке
def random_links():
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            hatnotes.append(element)
    try:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
    except Exception as e:
        print(f'Произошла ошибка - {e}')

#Метод для нового поискового запроса
def new_search():
    new_question = input('Что вы хотите найти?\n')
    search_field = browser.find_element(By.XPATH, "//input [@class = 'vector-search-box-input']")
    search_button = browser.find_element(By.XPATH, "//input [@id = 'searchButton']")
    search_field.send_keys(new_question)
    search_button.click()

#Основной цикл для работы с программой
while True:
    user_choice = input('Введите номер следующего действия следующее действие: \n 1. Листать параграфы.\n 2. Перейти на случайную ссылку со страницы.\n '
                        '3. Поискать что-то новое.\n 4. Завершить программу\n')
    if user_choice == '1':
        read_paragrafs()
        print('Параграфы закончились')
    elif user_choice == '2':
        random_links()
    elif user_choice == '3':
        new_search()
    elif user_choice == '4':
        browser.quit()
        break
    else:
        print('Введено не существующее значение. Попробуйте еще раз')