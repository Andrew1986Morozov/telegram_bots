import ptbot
import os
from pytimeparse import parse


TG_TOKEN = os.getenv("TELEGA_TOKEN")      # подставьте свой ключ API
TG_CHAT_ID = os.getenv("TELEGA_CHAT_ID")  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)

def wait(chat_id, question):
    bot.create_timer(parse(question), choose, author_id=chat_id, message=question)

def choose(author_id, message):
    answer = "Время вышло!"
    bot.send_message(author_id, answer)

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()
