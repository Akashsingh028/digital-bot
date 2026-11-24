import os
import threading
import telebot
import google.generativeai as genai
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- Render ke liye Port kholna (Ye sabse jaruri hai) ---
def run_server():
    port = int(os.environ.get("PORT", 10000))
    # Ek chota sa server jo Render ko batayega bot zinda hai
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is Live!")
        def log_message(self, format, *args):
            pass
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()

threading.Thread(target=run_server, daemon=True).start()
# ---------------------------------------------------------

# --- Keys lena ---
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_KEY = os.environ.get("GEMINI_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Namaste! 🙏 Main Digital Bot hu. Kuch bhi pucho!")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Thoda ruk jao, soch raha hu... phir se pucho!")

print("Bot Started...")
bot.infinity_polling()
