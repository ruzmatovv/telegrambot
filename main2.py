# from transliterate import to_latin, to_cyrillic
#
# print(to_latin("салом"))
# print(to_cyrillic("salom"))
#
# matn="salom"
#
# if matn.isascii():
#     print( to_cyrillic(matn))
#
# else:
#     print(to_latin(matn))

import asyncio
from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command
from transliterate import to_latin, to_cyrillic

from lotin import to_cyrillic

bot=Bot("123")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Kirill lotin botga hush kelibsiz")

@dp.message()
async def kirill_lotin(message:types.Message):
    matn=message.text
    if matn.isascii():
        await message.reply(to_cyrillic(matn))

    else:
        await message.reply(to_latin(matn))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())