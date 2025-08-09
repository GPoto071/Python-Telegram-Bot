import telebot
import random
from connections import bot
from db_handlers import choose_random, choose_random_only_rus
from telebot import types

def again_button(test):
    return types.InlineKeyboardButton('Заново', callback_data=f'{test}')

def tasks_button():
    return types.InlineKeyboardButton('К заданиям', callback_data='tasks')

def monetization_button():
    return types.InlineKeyboardButton('Поддержать автора', callback_data='monetization')

def stat_button():
    return types.InlineKeyboardButton('Статистика', callback_data='stat')

def menu_button():
    return types.InlineKeyboardButton('В главное меню', callback_data='menu')

def test1_button():
    return types.InlineKeyboardButton('Перевести слово', callback_data='test_id1')

def other_button():
    return types.InlineKeyboardButton('Остальные задания', callback_data='test_id')

def check(a, b):
    return 'right' if a == b else 'wrong'


@bot.callback_query_handler(func=lambda callback: True)  # Функции
def callback_message(callback):
        markup = types.InlineKeyboardMarkup()
        match callback.data:
            case 'menu':  #
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = tasks_button()
                btn2 = monetization_button()
                btn3 = stat_button()
                markup.row(btn1, btn2)
                markup.row(btn3)
                bot.send_message(callback.message.chat.id,
                         f'Вы в главном меню.',
                         reply_markup=markup)

            case 'tasks': # Задания
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = test1_button()
                btn2 = other_button()
                btn3 = menu_button()
                markup.row(btn1)
                markup.row(btn2)
                markup.row(btn3)
                bot.send_message(callback.message.chat.id, 'Выберите задание из списка:', reply_markup=markup)

            case 'test_id':  # Остальные задания
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = monetization_button()
                btn2 = menu_button()
                markup.row(btn1, btn2)
                bot.send_message(callback.message.chat.id,
                             'Задания пока ещё не готовы, но скоро будут, поддержите автора для того, чтобы они вышли скорее...',
                             reply_markup=markup)

            case 'test_id1': #Слово - значение
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                fake1, fake2, fake3 = choose_random_only_rus(), choose_random_only_rus(), choose_random_only_rus()
                global eng, rus
                eng, rus = choose_random()
                spisochek = [fake1, fake2, fake3, rus]
                random.shuffle(spisochek)
                btn1 = types.InlineKeyboardButton(f'{spisochek[0]}', callback_data=check(spisochek[0], rus))
                btn2 = types.InlineKeyboardButton(f'{spisochek[1]}', callback_data=check(spisochek[1], rus))
                btn3 = types.InlineKeyboardButton(f'{spisochek[2]}', callback_data=check(spisochek[2], rus))
                btn4 = types.InlineKeyboardButton(f'{spisochek[3]}', callback_data=check(spisochek[3], rus))
                markup.row(btn1, btn2)
                markup.row(btn3, btn4)
                btn5 = menu_button()
                markup.row(btn5)
                bot.send_message(callback.message.chat.id,
                         f"Какому слову соответствует перевод слова {eng}?", reply_markup=markup)

            case 'stat':  # Функция статистики
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = monetization_button()
                btn2 = menu_button()
                markup.row(btn1, btn2)
                bot.send_message(callback.message.chat.id,
                             'Статистика пока ещё не готова, но сразу будет после заданий, поддержите автора для того, чтобы всё вышло быстрее 🚧🔨',
                             reply_markup=markup)

            case 'monetization':  # Функция поддержать автора
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = menu_button()
                markup.row(btn1)
                bot.send_message(callback.message.chat.id,
                             'Пока что оплата доступна только по карте, однако вскоре способов оплаты будет больше 🔥'
                             '                                         Реквизиты ТИНЬКОФФ: 5536 9141 7726 1710',
                             reply_markup=markup)

            case 'right':
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = menu_button()
                btn2 = monetization_button()
                btn3 = tasks_button()
                btn4 = again_button('test_id1')
                markup.row(btn1, btn2)
                markup.row(btn3, btn4)
                bot.send_message(callback.message.chat.id,
                         f'Задание выполнено верно ✅',
                         reply_markup=markup)

            case 'wrong':
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                btn1 = menu_button()
                btn2 = monetization_button()
                btn3 = tasks_button()
                btn4 = again_button('test_id1')
                markup.row(btn1, btn2)
                markup.row(btn3, btn4)
                bot.send_message(callback.message.chat.id,
                         f'Задание выполнено неверно❌Правильный ответ: ' + f'{rus}' + 'Попробовать ещё раз?',
                         reply_markup=markup)