import os
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = f'{os.getenv("API_HASH")}'
hh_chat_id = os.getenv("HH_CHAT_ID")

app = Client("Assistant", api_id, api_hash)


@app.on_message(filters.chat(int(hh_chat_id)))
async def handle_message(app, message):
    if message.text:
        response = await get_response(message.text)
        await app.send_message(message.chat.id, response)


async def get_response(message):
    if "Поднять снова через 4 часа?" in message:
        return "Поднять"
    elif "Новое со времени вашего последнего визита" in message:
        return "Поднять резюме в поиске"


async def main():
    await app.start()


app.run()
