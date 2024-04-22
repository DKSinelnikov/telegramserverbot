import telebot

bot = telebot.TeleBot('7137092222:AAFGtOEsKnypcdO5-A2QIpZNZ5yaBWQOTWE')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро пожаловать!")

bot.polling()