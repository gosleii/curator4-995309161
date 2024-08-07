import telebot
bot = telebot.TeleBot("7425270251:AAE2XInPmwt2V_hZIEagO1zCXpE4TqBng4s")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Привет, бро")

bot.infinity_polling()