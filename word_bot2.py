import telebot
from telebot.types import Message
import random,os

API_TOKEN = os.environ.get('BOT_TOKEN')


bot = telebot.TeleBot(API_TOKEN)
smiles=['☹️',
'🙁',
'😠',
'😡',
'😞',
'😟',
'😣',
'😖']

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message:Message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['help'])
def send_help(message:Message):
      bot.reply_to(message,"I`m here to help")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def upper(message):
    bot.reply_to(message,random.choice(smiles))
#def echo_message(message):
   # bot.reply_to(message, message.text)


bot.polling()