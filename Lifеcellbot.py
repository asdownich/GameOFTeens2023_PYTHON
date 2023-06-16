from aiogram import Dispatcher, Bot, types, executor
import logging

bot = Bot("6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.username}</b>"
    await message.answer(f"Привіт, {user_tag}! Я бот від Lifеcellbot тут ви можете оплати тариф і тд ",
                         parse_mode='HTML')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Тариф 1'))
    keyboard.add(KeyboardButton('Тариф 2'))
    keyboard.add(KeyboardButton('Тариф 3'))
    keyboard.add(KeyboardButton('Тариф 4'))
    keyboard.add(KeyboardButton('Тариф 5'))
    await message.answer('Виберіть тариф:', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
