# Попробуйте решить данные задачу без помощи нейросетей
# Напишите программу на Python с использованием модуля tkinter,
# которая позволяет пользователю ввести свое имя в окно ввода, а затем выводит на экран сообщение "Привет, [имя]!".

import tkinter as tk
#Создание функции для работы кнопки
def greeting():
    greeting_label.config(text=f'Привет, {name.get()}!')

root = tk.Tk()
#Задание размера и название окна
root.geometry('400x400')
root.title('Программа с использованием tkinter')


#Создание поля для ввода имени и подписи к этому полю
name_label = tk.Label(text='Введите имя в поле ниже')
name_label.pack()
name = tk.Entry()
name.pack()

#Создание кнопки приветствия
greeting_button = tk.Button(root, text='Поприветствовать', command=greeting)
greeting_button.pack()

#Создание виджета приветствия
greeting_label = tk.Label()
greeting_label.pack()

#Зацикливание окна
root.mainloop()