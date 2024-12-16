from aiogram import Bot, Dispatcher, types
from asyncio import run


async def echo(message:types.Message):
    await message.reply(message.text)

dp = Dispatcher()

async def start():
    dp.message.register(echo)
    bot=Bot("7594670214:AAFIO4iaiadNiP6G03-iRyNvWq_0fQosVpk")
    await dp.start_polling(bot)

run(start())