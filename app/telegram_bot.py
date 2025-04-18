import os
import aiohttp
from dotenv import load_dotenv
import ssl
import requests



load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# async def send_telegram_message(text: str):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
#     payload = {"chat_id": CHAT_ID, "text": text}
#     async with aiohttp.ClientSession() as session:
#         await session.post(url, data=payload)



async def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot6494999568:AAHFXX78-HLOepszO9r8PfxI1EqD2hCA390/sendMessage"
    payload = {
        'chat_id': 908977119,
        'text': message
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            # Вы можете проверить статус ответа и обработать ошибки, если необходимо
            if response.status == 200:
                return await response.json()  # или другая обработка ответа
            else:
                return await response.text()


