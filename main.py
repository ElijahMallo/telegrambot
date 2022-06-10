import telebot

TOKEN = "5357661899:AAEjJnq9M7boQ2_jow6W6jf6PRmoLmhV88g"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message ):
    text = 'Чтобы начать работу введите команду в формате: \<имя волюты> \ <в какую валюту перевести> \ <количество валюты>'
    bot.reply_to(message, text)

bot.polling(none_stop=True)