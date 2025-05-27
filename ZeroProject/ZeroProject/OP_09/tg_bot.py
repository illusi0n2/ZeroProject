import time
import telebot
from datetime import datetime
from task import Task
import threading
import re


bot = telebot.TeleBot('7485941819:AAG_uTMGLcvNnMFD2a4YX7bHPDtU3cx_tHA')
tasks_list = [Task('123', '28-05-2025 12:50'), Task('123', '28-05-2025 12:55'), Task('fdsfsdf', '28-05-2025 12:50'), Task('utyutyutyu', '28-05-2025 12:50')]
matches = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет!')
    tread = threading.Thread(target=send_reminder, args=(message.chat.id,))
    tread.start()

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, 'Вот список доступных команд')


@bot.message_handler(commands=['new'])
def create_task(message):
    msg = bot.reply_to(message, "Введи название дела")
    bot.register_next_step_handler(msg, task_name_step)

@bot.message_handler(commands=['tasks_list'])
def show_all_tasks(message):
    msg = ""
    for i in range(len(tasks_list)):
        msg += f'Напоминание о {tasks_list[i].get_name()} установлено на {tasks_list[i].get_date()} \r'
    bot.reply_to(message, msg)

@bot.message_handler(commands=['delete_task'])
def delete_message(message):
    msg = bot.reply_to(message, "Введи название задачи, которую хочешь удалить")
    bot.register_next_step_handler(msg, chek_task)



def task_name_step(message):
    try:
        task_name = message.text

        msg = bot.reply_to(message, 'Введи дату напоминания в формате - DD-MM-YYYY hh:mm.\r Пример - 31-01-1999 09:00')
        bot.register_next_step_handler(msg, task_date_step, task_name)

    except ValueError as e:
        bot.reply_to(message, "Ошибка: " + str(e))
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка")
        print(f"Ошибка: {e}")

def task_date_step(message, task_name):
    try:
        date = message.text
        if not validate_datetime(date):
            bot.reply_to(message, 'Не верный формат даты. Попробуй еще')
            bot.register_next_step_handler(message, task_date_step)
        else:
            if is_valid_datetime(date):
                bot.reply_to(message, f'Напоминание установлено на {date}')
                created_task = Task(task_name, date)
                tasks_list.append(created_task)
            else:
                bot.reply_to(message, f'Даты {date} не существует. Попробуй еще раз')
                bot.register_next_step_handler(message, task_date_step)

    except ValueError as e:
        bot.reply_to(message, "Ошибка: " + str(e))
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка")
        print(f"Ошибка: {e}")
def chek_task(message):
    task = message.text
    for i in range(len(tasks_list)):
        if tasks_list[i].get_name() == task:
            matches.append(i)
    msg = f'У тебя {len(matches)} задач с таким названием.\n '
    if len(matches) > 1:
        for i in range(len(matches)):
            msg += f'{i+1}. {tasks_list[matches[i]].get_name()} установлено на {tasks_list[matches[i]].get_date()}\n '
        msg += 'Выбери номер какое напоминание удалить?'
        bot.reply_to(message, msg)
        bot.register_next_step_handler(message, delete_task,-1)
    else:
        del tasks_list[matches[0]]
        bot.reply_to(message, 'Напоминание удалено')
        matches.clear()
def delete_task(message, index):
    try:
        i = int(message.text)
        del tasks_list[matches[i-1]]
        bot.reply_to(message, 'Напоминание удалено')
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка")
        print(f"Ошибка: {e}")
    matches.clear()

def validate_datetime(date_string):
    pattern = re.compile(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$')
    if pattern.match(date_string):
        return True
    return False

def is_valid_datetime(date_string):
    try:
        datetime.strptime(date_string, '%d-%m-%Y %H:%M')
        return True
    except ValueError:
        return False

def send_reminder(chat_id):
    while True:
        now = datetime.now().strftime('%d-%m-%Y %H:%M')
        for i in range(len(tasks_list)):
            if tasks_list[i].get_date() == now:
                bot.send_message(chat_id, f'Напоминание о {tasks_list[i].get_name()}')
                time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)