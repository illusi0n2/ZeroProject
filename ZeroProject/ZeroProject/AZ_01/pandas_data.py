# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets
#
#  Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз

import pandas as pd

#Выполнение п.1 из постановки дз
df = pd.read_csv('airlines_flights_data.csv')

print(df.head())
print(df.info())
print(df.describe())

#Выполнение п.2
df_dz = pd.read_csv('dz.csv')
salary_grouped = df.groupby('City')['Salary'].mean()

print(salary_grouped)