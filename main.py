import telebot
from telebot import types


bot = telebot.TeleBot("6620288649:AAEpvZYh6VikZNk2bx9_u7GsPlzRjQYTZHg")

# Обработчики команд
@bot.message_handler(commands = ['start'])
def get_started(message):
    bot.send_message(message.from_user.id, 
                     "Добро пожаловать в чат с моим телеграм-ботом!\nДля дополнительной информации пиши /help .")


@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.from_user.id, """/last_selfie - Мое последнее селфи\n/school_photo - Мое фото из старшей школы\n/voices - Меню для получения голосовых сообщений\n/rep_url - Ссылка на проект""")
      
      
@bot.message_handler(commands = ['last_selfie'])
def send_selfie(message):
    bot.send_photo(message.from_user.id,photo=open('images/selfie.jpg', 'rb'))


@bot.message_handler(commands = ['school_photo'])
def send_selfie(message):
    bot.send_photo(message.from_user.id,photo=open('images/school_photo.jpg', 'rb'))


@bot.message_handler(commands = ['voices'])
def open_voice_menu(message):
    # Создание кнопок для получения голосовых сообщений
    keybord = types.InlineKeyboardMarkup()

    key_gpt = types.InlineKeyboardButton(text='О GPT',callback_data='gpt')
    keybord.add(key_gpt)

    key_db = types.InlineKeyboardButton(text='NoSQL и SQL',callback_data='about_db')
    keybord.add(key_db)

    key_first_love = types.InlineKeyboardButton(text='Про первую любовь',callback_data='first_love')
    keybord.add(key_first_love)
    bot.send_message(message.from_user.id,"Выберите голосовое:", reply_markup=keybord)


@bot.message_handler(commands = ['rep_url'])
def send_selfie(message):
    bot.send_message(message.from_user.id,"https://github.com/antonnurapkin/telegram_bot.git")

# Обработчик нажатий кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'gpt':
        bot.send_audio(call.message.chat.id,audio=open('sounds/О GPT.wav', 'rb'))
    elif call.data == 'about_db':
        bot.send_audio(call.message.chat.id,audio=open('sounds/NoSQL и SQL.wav', 'rb'))
    elif call.data == 'first_love':
        bot.send_audio(call.message.chat.id,audio=open('sounds/О первой любви.wav', 'rb'))


bot.infinity_polling()