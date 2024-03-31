from main import coinmarket_api_key, weather_api_key, default_city
from keyboards import main_keyboard
from main import bot
from inline import contacts_list
import httpx


async def start(message):
    await message.answer(text=f'Hello, {message.from_user.first_name}, I`m glad to see ya', reply_markup=main_keyboard)


async def dice(message):
    await bot.send_dice(chat_id=message.chat.id, emoji='🎲')


async def basketball(message):
    await bot.send_dice(chat_id=message.chat.id, emoji='🏀')


async def bowling(message):
    await bot.send_dice(chat_id=message.chat.id, emoji='🎳')


async def list_of_contacts(message):
    await message.answer('\n===================================='
                         '\n  🌝There my creator`s contacts🌚'
                         '\n====================================',
                         reply_markup=contacts_list)


async def weather(message):
    city = default_city
    if len(message.text.split()) > 3:
        city = message.text.split()[1]
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        reply = f'✅ Weather in {city}:\n' \
                f'☁ Sky: {weather_description}\n' \
                f'🌡 Temperature is: {temp}°C\n' \
                f'💧 Humidity: {humidity}%\n' \
                f'💨 Wind speed is: {wind_speed} m/s'
    else:
        reply = 'Failed to show weather data'
    await message.answer(f'{reply}')


async def bitcoin(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': coinmarket_api_key
    }
    parameters = {
        'symbol': 'BTC'
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=parameters)
    data = response.json()
    if 'data' in data:
        price = data['data']['BTC']['quote']['USD']['price']
        reply = f'✅ Current bitcoin rate: ${price:.2f}'
    else:
        reply = 'Failed to get data on the bitcoin rate'
    await message.answer(f'{reply}')


async def etherium(message):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': coinmarket_api_key
    }
    parameters = {
        'symbol': 'ETH'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=parameters)
    data = response.json()

    if 'data' in data:
        price = data['data']['ETH']['quote']['USD']['price']
        reply = f'✅ Current etherium rate: ${price:.2f}'
    else:
        reply = 'Failed to get data on the etherium rate'
    await message.answer(f'{reply}')
