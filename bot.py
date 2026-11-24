import telebot

TOKEN = "9138736075:AAERLfEl1Aa74PTt-FT9uObnt-JsqznQ6x4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🌍 Welcome to The Digital World!\nBy Akash\n\n/joke - Joke 😂\n/motivation - Quote 💪\n/youtube - Channel ▶️")

@bot.message_handler(commands=['joke'])
def joke(message):
    bot.reply_to(message, "Teacher: Homework kyu nahi kiya?\nStudent: Sir Light chali gayi thi! 😂")

@bot.message_handler(commands=['motivation'])
def motivation(message):
    bot.reply_to(message, "💪 Mehnat itni chup chap karo ki Safalta shor macha de!")

@bot.message_handler(commands=['youtube'])
def youtube(message):
    bot.reply_to(message, "▶️ Subscribe karo: https://www.youtube.com/@thedigitalworld28")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Samajh nahi aaya! /start likho 😅")

print("Bot Chal Gaya!")
bot.polling()
