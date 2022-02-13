import ptbot
import os
import random


TG_TOKEN = os.getenv("TELEGA_TOKEN")      # подставьте свой ключ API
TG_CHAT_ID = os.getenv("TELEGA_CHAT_ID")  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)
bot.send_message(TG_CHAT_ID, "Привет!")
bot.send_message(TG_CHAT_ID, "Как дела?")

def wait(chat_id, question):
    bot.create_timer(5, choose, author_id=chat_id, message=question)

def choose(author_id, message):
    answers = ("да", "нет", "это возможно")
    choice = random.choice(answers)
    answer = "Думаю, {}".format(choice)
    bot.send_message(author_id, answer)
    print("Мне написал пользователь с ID:", author_id)
    print("Он спрашивал:", message)
    print("Я ответил:", answer)

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()
