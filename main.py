from aiogram import Dispatcher, Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio
import logging
import time
import requests


rtr = Router()

logging.basicConfig(level=logging.INFO)
# Bu yerga OpenWeatherMap API kalitingizni kiriting
OPENWEATHER_API_KEY = '28e4d8851ad368eede65bffbe0b89a8c'
# Bu yerga o'z bot tokeningizni kiriting
TELEGRAM_BOT_TOKEN = '7477811318:AAFrKusFAqIzmdftbMtxbT2PdQX-FC9f41A'


def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric&lang=uz"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return "Shahar topilmadi. Iltimos, shahar nomini tekshirib qayta kiriting."

    city = data['name']
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    weather_info = (
        f"🏙️ Shahar: {city}\n"
        f"🌤️ Holat: {weather_description}\n"
        f"🌡️ Harorat: {temperature}°C\n"
        f"💧 Namlik: {humidity}%\n"
        f"🌬️ Shamol tezligi: {wind_speed} m/s\n"
    )
    return weather_info

@rtr.message(Command("start"))
async def star_command(message: Message):
    await message.answer("asdasd")

@rtr.message()
async def msg(msg:Message):
    sity_name = msg.text
    wather_info = get_weather(sity_name)
    await msg.reply(wather_info)


async def main():
    bot = Bot(token='7743716265:AAGrbIWlnl4THhqQt2HEkIceiRErYkxrU_I')
    dp = Dispatcher()
    dp.include_router(rtr)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def times():
    time_time = time.time()
    local_time = time.localtime(time_time)
    format_time = time.strftime('%m-%d | %H:%M, local_time')
    return local_time


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print(f"start bot")
        asyncio.run(main())
    except KeyboardInterrupt:
        print('stop')
