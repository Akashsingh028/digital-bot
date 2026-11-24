import os
import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = os.environ.get("9138736075:AAERLfEl1Aa74PTt-FT9uObnt-JsqznQ6x4")
GEMINI_KEY = os.environ.get("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
bot = telebot.TeleBot(9138736075:AAERLfEl1Aa74PTt-FT9uObnt-JsqznQ6x4)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Namaste! Mai Digital World AI Bot hun!\nBy Akash\n\nKuch bhi pucho, mai jawab dunga!\nJaise - Shayari sunao, Padhai me madad karo, Joke sunao")

@bot.message_handler(func=lambda m: True)
def ai_reply(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Thoda ruk jao, AI soch raha hai... Dobara try karo! 😅")

print("AI Bot Chal Gaya!")
bot.polling()
