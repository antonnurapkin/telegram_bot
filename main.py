import telebot
from telebot import types


bot = telebot.TeleBot("6620288649:AAEpvZYh6VikZNk2bx9_u7GsPlzRjQYTZHg")

@bot.message_handler(commands = ['start'])
def get_started(message):
    bot.send_message(message.from_user.id, 
                     """Добро пожаловать в чат с моим телеграм-ботом!
                     Для дополнительной информации пиши /help .""")

@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.from_user.id, """/last_selfie - Мое последнее селфи\n/school_photo - Мое фото из старшей школы\n/voice - Мой рассказ обо всём\n/rep_url - Ссылка на проект""")
    
@bot.message_handler(commands = ['last_selfie'])
def send_selfie(message):
    bot.send_photo(message.from_user.id,photo=open('images/selfie.jpg', 'rb'))

@bot.message_handler(commands = ['school_photo'])
def send_selfie(message):
    bot.send_photo(message.from_user.id,photo=open('images/school_photo.jpg', 'rb'))


@bot.message_handler(commands = ['voice'])
def send_selfie(message):
    bot.send_audio(message.from_user.id,audio=open('sounds/about_db.wav', 'rb'))

bot.infinity_polling()