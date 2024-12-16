import asyncio
from aiogram import Bot, Dispatcher,types,F
from aiogram.filters import Command

bot = Bot(token="7558451732:AAEcyBqFYu_SkdVIjiOShoAMpix22xr5KyU")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Botga hush kelibsiz")

@dp.message(Command("user_info"))
async def info(message:types.Message):
    await message.answer(f" Mening ID im{str(message.from_user.id)}")

@dp.message(F.text=="salom")
async def salom(message:types.Message):
    await message.reply("Va aleykum")

@dp.message(F.text=="qandaysan")
async def salom(message:types.Message):
    await message.reply("Men yaxshiman")

@dp.message(F.text == "menga yordam ber")
async def salom(message: types.Message):
    await message.reply("Sizga qanday yordam bera olaman")

@dp.message(F.text == "men bilan gaplasha olasanmi")
async def salom(message: types.Message):
    await message.reply("Ha albatta")


@dp.message(F.text == "bu bot orqali nimalar qilish mumkin")
async def salom(message: types.Message):
    await message.reply("Siz bot bilan gaplashishishingiz va rasmlar olishingiz mumkin")


@dp.message(Command("rasm1"))
async def get_photo(message:types.Message):
    await message.answer_photo(photo="https://i.insider.com/5466790becad0466416c845d", caption="Rasm")


@dp.message(Command("rasm2"))
async def get_photo(message:types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-altay/5534173/2a0000018633eca0c8aee41be6634d67f753/XXL_height", caption="Rasm")

@dp.message(Command("rasm3"))
async def get_photo(message:types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/h6WQSElaBjE/maxresdefault.jpg", caption="Rasm")


@dp.message(Command("rasm4"))
async def get_photo(message:types.Message):
    await message.answer_photo(photo="https://earthsky.org/upl/2020/09/Celestia-Europe-Io-Jupiter-800x500.jpg", caption="Rasm")


@dp.message(Command("rasm5"))
async def get_photo(message:types.Message):
    await message.answer_photo(photo="https://i.insider.com/5c7ebf89dde8671b6415877d?width=2000&format=jpeg&auto=webp", caption="Rasm")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

