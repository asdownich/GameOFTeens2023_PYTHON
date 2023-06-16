from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Dispatcher, Bot, types, executor
import logging

bot = Bot("6128664648:AAEPCBcwaF1SckoPdio4YoRfLFRRRtxK7bk")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

main_menu_buttons = [
    KeyboardButton('Меню'),
    KeyboardButton('Тариф'),
    KeyboardButton('Помощ')
]

tariff_buttons = [
    KeyboardButton('Вільний Лайф'),
    KeyboardButton('Смарт Лайф'),
    KeyboardButton('Просто Лайф'),
    KeyboardButton('Platinum Лайф'),
    KeyboardButton('Шкільний Лайф'),
    KeyboardButton('Шкільний Лайф'),
    KeyboardButton('Ґаджет'),
    KeyboardButton('Смарт Сімя'),
    KeyboardButton('Назад')
]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.username}</b>"
    await message.answer(f"Привіт, {user_tag}! Я бот від Lifеcellbot тут ви можете оплатити тариф і тд ",
                         parse_mode='HTML')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)


@dp.message_handler(text='Тариф')
async def show_tariffs(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*tariff_buttons)
    await message.answer('Виберіть тариф:', reply_markup=keyboard)


@dp.message_handler(text='Назад')
async def go_back(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
