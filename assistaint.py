import os
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = f'{os.getenv("API_HASH")}'
hh_chat_id = os.getenv("HH_CHAT_ID")

app = Client("Assistant", api_id, api_hash)


@app.on_message(filters.chat(int(hh_chat_id)))
def handle_message(app, message):
    if "Поднять снова через 4 часа?" in message.text:
        app.send_message(int(hh_chat_id), "Поднять")
    elif "Новое со времени вашего последнего визита" in message.text:
        app.send_message(int(hh_chat_id), "Поднять резюме в поиске")


app.run()
