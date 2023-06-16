from aiogram import Dispatcher, Bot, types, executor
import logging

bot = Bot("6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)
