import telebot
import requests

bot = telebot.TeleBot('5855640404:AAFcIc16j9nPjP_j9Df1jJH96e__kHIekBk')
API_URL = "http://127.0.0.1:8000/api/user/"
query = {
    "tokedn": "",
    "chat_id": ""
}


@bot.message_handler(content_types=['text'])
def get_messages(message):
    print(message.text)
    print(bot.get_chat(message.from_user.id).id)
    query["token"] = message.text
    query["chat_id"] = bot.get_chat(message.from_user.id).id
    response = requests.post(API_URL, json=query)
    print(response.status_code)
    if response.status_code == 200:
        print(response.json())


bot.polling(none_stop=True, interval=0)
