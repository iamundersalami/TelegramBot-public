import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from handlers import *


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO,)
logging.getLogger("aiogram").setLevel(logging.INFO)
logging.getLogger("httpx").setLevel(logging.ERROR)

dp = Dispatcher()
telegram_bot_token = 'your token'
bot = Bot(token=telegram_bot_token)
weather_api_key = 'your token'
coinmarket_api_key = 'your token'
default_city = 'your city'


async def main():
    dp.message.register(start, Command("start"))
    dp.message.register(dice, F.text == '🎲 Dice 🎲')
    dp.message.register(basketball, F.text == '🏀 Basketball 🏀')
    dp.message.register(bowling, F.text == '🎳 Bowling 🎳')
    dp.message.register(bitcoin, F.text == '💰 Bitcoin 💰')
    dp.message.register(etherium, F.text == '🔷 Etherium 🔷')
    dp.message.register(weather, F.text == '☀ Weather ☀')
    dp.message.register(list_of_contacts, F.text == '🌐 Contacts 🌐')

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
