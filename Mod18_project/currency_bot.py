import telebot


TOKEN = ""

bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)
