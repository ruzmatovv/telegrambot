import asyncio
from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command
import requests

bot = Bot(token="7786570917:AAGV-6lkyOBK2cGyRjXI33dpozHWJYZbFhM")
dp = Dispatcher()

API_KEY = "e672957957c7913bcee6d1d4b949317e"

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("ob-havo botga hush kelibsiz")

@dp.message()
async def weather(message:types.Message):
    city_name = message.text
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    temp = data['main'] ['temp']
    await message.reply(f"🌤 Shahar: {data['name']}\n"
                            f"🌡 Temperatura: {temp}°C\n")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
