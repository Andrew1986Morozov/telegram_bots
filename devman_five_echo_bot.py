import ptbot
import os


TG_TOKEN = os.getenv("TELEGA_TOKEN")      # подставьте свой ключ API
TG_CHAT_ID = os.getenv("TELEGA_CHAT_ID")  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)

def choose(author_id, message):
    bot.send_message(author_id, message)

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(choose)
bot.run_bot()
