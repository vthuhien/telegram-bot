
from telegram._update import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from flask import Flask
from threading import Thread
import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get("TOKEN")

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user.first_name
    await update.message.reply_text(
        f"Hi {user}, shop đã nhận được tin nhắn của bạn và sẽ phản hồi sớm nhất!"
    )

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is alive"

def run():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == '__main__':
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_message))
    print("Bot is running...")
    app.run_polling()
