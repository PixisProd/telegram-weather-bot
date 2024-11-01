from fastapi import FastAPI
from aiogram import types
from config import TELEGRAM_BOT_TOKEN, NGROK_TUNNEL_URL
from bot import bot, dp


app = FastAPI()

TELEGRAM_BOT_URL = f'/bot/{TELEGRAM_BOT_TOKEN}'
BOT_FULL_URL = f'{NGROK_TUNNEL_URL}{TELEGRAM_BOT_URL}'

@app.on_event('startup')
async def startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != BOT_FULL_URL:
        await bot.set_webhook(url=BOT_FULL_URL)

@app.post(TELEGRAM_BOT_URL)
async def get_updates(upd: dict):
    telegram_update = types.Update(**upd)
    await dp.feed_update(bot=bot, update=telegram_update)

@app.on_event('shutdown')
async def shutdown():
    await bot.session.close()