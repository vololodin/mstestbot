
import telebot
from telebot import types


TOKEN = '1830425110:AAGYIMXXspdB63zTy5Wz-aPcbXQ6vQx3jpA'

bot = telebot.TeleBot(TOKEN)
pol = ''
act = 0
wght = 0

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
key_m = types.KeyboardButton('мужской')
key_j = types.InlineKeyboardButton('женский')
keyboard.add(key_m, key_j)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Добро пожаловать, для начала расчета необходимо определить твой пол"
                                            , reply_markup=keyboard)
        bot.register_next_step_handler(message, get_pol)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def get_pol(message):
    global pol
    pol = message.text
    bot.send_message(message.from_user.id, 'Сколько часов в день вы физически активны?')
    bot.register_next_step_handler(message, get_act)

def get_act(message):
        global act
        while act == 0:
            try:
                act = int(message.text)
            except Exception:
                bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        act = int(message.text)
        bot.send_message(message.from_user.id, 'Сколько вы весите?')
        bot.register_next_step_handler(message, get_wght)

def get_wght(message):
        global wght
        while wght == 0:
            try:
                wght = int(message.text)
            except Exception:
                bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

        bot.send_message(message.from_user.id, 'Вам необходимло выпивать'+'  '+str(wght*0.03+act*0.5)+'  '+'литра воды в день')

        keyboard1 = types.InlineKeyboardMarkup (row_width=2)
        key_yes = types.InlineKeyboardButton(text='Да',callback_data='yes')
        keyboard1.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет',callback_data='no')
        keyboard1.add(key_no)
        question = 'Попробуем ещё раз?'
        bot.send_message(message.from_user.id, text = question, reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Напиши /start')

    elif call.data == "no":
        bot.send_message(call.message.chat.id, "have a good day")


bot.polling(timeout=60)