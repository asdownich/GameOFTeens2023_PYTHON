from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher, Bot, types, executor
import logging

bot = Bot("6128664648:AAEPCBcwaF1SckoPdio4YoRfLFRRRtxK7bk")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

main_menu_buttons = [
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

tariff_descriptions = {
    'Вільний Лайф': 'Опис Вільний Лайф',
    'Смарт Лайф': 'Опис Смарт Лайф',
    'Просто Лайф': 'Опис Просто Лайф',
    'Platinum Лайф': 'Опис Platinum Лайф',
    'Шкільний Лайф': 'Опис Шкільний Лайф',
    'Ґаджет': 'Опис Ґаджет',
    'Смарт Сімя': 'Опис Смарт Сімя'
}


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


@dp.message_handler(text=[tariff for tariff in tariff_descriptions.keys()])
async def show_tariff_description(message: types.Message):
    tariff = message.text
    description = tariff_descriptions.get(tariff)
    await message.answer(f'{tariff}: {description}')


@dp.message_handler(text='Помощ')
async def help(message: types.Message):
    url = 'https://www.lifecell.ua/uk/pidtrimka/'
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Перейти до підтримки', url=url))
    await message.answer('Якщо вам потрібна додаткова допомога, перейдіть за посиланням нижче:', reply_markup=keyboard)


@dp.message_handler(text='Назад')
async def go_back(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
