import ptbot
import os
from pytimeparse import parse


TG_TOKEN = os.getenv("TELEGA_TOKEN")      # подставьте свой ключ API
TG_CHAT_ID = os.getenv("TELEGA_CHAT_ID")  # подставьте свой ID
chat_id = TG_CHAT_ID

def wait(TG_CHAT_ID, text_message):
    converter_text_to_time = parse(text_message)
    message_id = bot.send_message(chat_id, f"Запустить таймер на {converter_text_to_time} сек.")
    bot.create_countdown(converter_text_to_time, notify_progress, message_id=message_id, total_time=converter_text_to_time)
    bot.create_timer(converter_text_to_time, inform)

def notify_progress(secs_left, message_id, total_time):
    bot.update_message(chat_id, message_id, f"Осталось секунд: {secs_left}\n{render_progressbar(total_time, secs_left)}")

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def inform():
    bot.send_message(chat_id, "Время вышло!")


bot = ptbot.Bot(TG_TOKEN)
bot.send_message(chat_id, "На какое время запустить таймер?")
bot.reply_on_message(wait)
bot.run_bot()
