from connections import conn, bot
from message_handlers import *

conn.close()

if conn:
    print("Подключено")


@bot.message_handler(commands=['start'])
def main(message):

        markup = types.InlineKeyboardMarkup()
        btn1 = tasks_button()
        btn2 = monetization_button()
        btn3 = stat_button()
        markup.row(btn1, btn2)
        markup.row(btn3)
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name}. Этот бот разработан специально для изучения английского языка. Начнём?',
                         reply_markup=markup)

bot.polling(non_stop=True)