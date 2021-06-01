
import telebot
from telebot import types


TOKEN = '1803001643:AAE3cE6hsAtL2Ic50gLjLPRSpNjGgCfOKUU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Давайте знакомиться! Укажите ваш пол для подсчета сутойчной нормы потребления воды', reply_markup=keyboard())


def keyboard():
	InlineMarkup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	Inlinebutton1 = types.InlineKeyboardButton('Мужчина')
	Inlinebutton2 = types.InlineKeyboardButton('Женщина')

	InlineMarkup.add(Inlinebutton1, Inlinebutton2)
	return InlineMarkup



if __name__ == "__main__":
	bot.polling(none_stop=True)
