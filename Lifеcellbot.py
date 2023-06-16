from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

bot = Bot("6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.full_name}</b>"
    await message.answer(f"Привіт, {user_tag}! Я бот від Lifеcellbot тут ви можете оплати тариф і тд ",
                         parse_mode='HTML')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Список тарифів.'))
    keyboard.add(KeyboardButton('Конструктор Тарифу.'))
    keyboard.add(KeyboardButton('Звернутися у підтримку.'))
    await message.answer('Виберіть пункт:', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
