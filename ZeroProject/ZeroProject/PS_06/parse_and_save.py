import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

url = "https://www.divan.ru/sankt-peterburg/category/svet"

driver.get(url)
time.sleep(3)

fixtures = driver.find_elements(By.XPATH, '//div[@class="WdR1o"]')

parsed_data = []

for fixture in fixtures:
    try:
        title = fixture.find_element(By.XPATH, './/span[@itemprop="name"]').text
        price = fixture.find_element(By.XPATH, './/div[@class="pY3d2"]//span').text
        fixture_url = fixture.find_element(By.XPATH, './/div[@class="lsooF"]//link').get_attribute('href')
    except Exception as e:
        print (f'При парсинге произошла ошибка {e}')
        continue

    parsed_data.append([title, price, fixture_url])

driver.quit()


with open("fixtures.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)