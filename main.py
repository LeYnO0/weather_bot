import telebot
import requests
import json

from settings import *

bot = telebot.TeleBot(TELEGRAMM_TOKEN)
headers = {"X-Yandex-API-Key": "99316ae4-d3d6-4b9d-ad8d-9eea5b5b0942"}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=f"Я - бот с актуальными данными о погоде)\nВыберите команду:{COMMANDS_LINE}")


@bot.message_handler(commands=['pogodabsk'])
def pogodabsk(message):
    r = requests.get(url=BSK_URL, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        fact = data["fact"]
        bot.send_message(message.chat.id,
                         text=f'Сейчас в городе {fact["temp"]}°, ощущается как {fact["feels_like"]}°. Небо: {fact["condition"]}')
    else:
        bot.send_message(message.chat.id, 'Problems on weather API')


@bot.message_handler(commands=['pogodabrn'])
def pogodabrn(message):
    r = requests.get(url=BRN_URL, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        fact = data["fact"]
        bot.send_message(message.chat.id,
                         text=f'Сейчас в городе {fact["temp"]}°, ощущается как {fact["feels_like"]}°. Небо: {fact["condition"]}')
    else:
        bot.send_message(message.chat.id, 'Problems on weather API')


@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, text=f'Список доступных команд: {COMMANDS_LINE}')


bot.polling(none_stop=True)


# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()
