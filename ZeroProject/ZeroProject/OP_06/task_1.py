'''Задание 1. Создание и запись в файл

Напишите скрипт, который запрашивает у пользователя текст,
а затем записывает этот текст в файл `user_data.txt`.'''

#Сохраняем в файл введенный пользователем текст
text = input('Введите текст для записи в файл: ')

#Открываем файл
with open("user_data.txt", "w") as file:
    #Запись введенной пользователем строки в файл
    file.write(text)



