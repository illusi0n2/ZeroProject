import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
print("1. Гистограмма нормального распределения")

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(alpha=0.3)
plt.show()

print(f"Среднее значение: {np.mean(data):.3f}")
print(f"Стандартное отклонение: {np.std(data):.3f}")
print(f"Минимальное значение: {np.min(data):.3f}")
print(f"Максимальное значение: {np.max(data):.3f}")


print("\n2. Диаграмма рассеяния для двух наборов случайных данных")

np.random.seed(42)
x_data = np.random.rand(50)
y_data = np.random.rand(50)


plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.6, color='red', s=50)
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X значения (случайные)')
plt.ylabel('Y значения (случайные)')
plt.grid(alpha=0.3)
plt.show()


print("\nДемонстрация генерации случайного массива:")
random_array = np.random.rand(5)
print("Случайный массив из 5 чисел:", random_array)


print(f"\nСтатистика для X данных:")
print(f"Среднее: {np.mean(x_data):.3f}, Стандартное отклонение: {np.std(x_data):.3f}")
print(f"\nСтатистика для Y данных:")
print(f"Среднее: {np.mean(y_data):.3f}, Стандартное отклонение: {np.std(y_data):.3f}")
print(f"\nКорреляция между X и Y: {np.corrcoef(x_data, y_data)[0, 1]:.3f}")


#По заданию 3 парсер не работает на сайте, похоже на то, что на сайте какая-то защита стоит, поэтому использовал csv файл с прошлых уроков
df = pd.read_csv('light.csv')

# Преобразуем цены в числа (удаляем "руб." и пробелы)
df['Цена_число'] = df['Цена'].apply(lambda x: int(re.sub(r'[^\d]', '', str(x).replace(' ', ''))))

# Вычисляем среднюю цену
average_price = df['Цена_число'].mean()
print(f"Средняя цена на светильники: {average_price:,.0f} руб.")

# Создаем гистограмму
plt.figure(figsize=(10, 6))
plt.hist(df['Цена_число'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(average_price, color='red', linestyle='--', linewidth=2, label=f'Средняя: {average_price:,.0f} руб.')
plt.title('Гистограмма цен на светильники')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.legend()
plt.grid(alpha=0.3)
plt.show()