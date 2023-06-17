#сделать ссылку на покупку тарифов под их описаниями
#сделать конструктор тарифа по примеру с сайта: https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/
#косметическая доработка бота(кнопки назад, текст)
#проверка, при необходимости доработка
#запись екрана с работой бота
#собрать всё в файл на гитхабе и мы полностью готовы
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher, Bot, types, executor
import logging

BOT_TOKEN = Bot("6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo")
dp = Dispatcher(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

main_menu_buttons = [
    KeyboardButton('Обрати Тариф'),
    KeyboardButton('Створити свій тариф'),
    KeyboardButton('Підтримка')
]

tariff_buttons = [
    KeyboardButton('Вільний Лайф'),
    KeyboardButton('Смарт Лайф'),
    KeyboardButton('Просто Лайф'),
    KeyboardButton('Platinum Лайф'),
    KeyboardButton('Шкільний Лайф'),
    KeyboardButton('Ґаджет'),
    KeyboardButton('Смарт Сімя'),
    KeyboardButton('Назад')
]

gadjet_buttons = [
    KeyboardButton('Ґаджет Безпека'),
    KeyboardButton('Ґаджет Смарт'),
    KeyboardButton('Ґаджет Планшет'),
    KeyboardButton('Ґаджет Роутер')
]

tariff_descriptions = {
    'Вільний Лайф': '\n180 грн на місяць\nБезлімітний інтернет\n1600 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
    'Смарт Лайф': '\n120 грн на місяць\n25 ГБ інтернетy\n800 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
    'Просто Лайф': '\n90 грн на місяць\n8 ГБ інтернетy\n300 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
    'Platinum Лайф': '\n250 грн на місяць\nБезлімітний інтернет\n3000 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
    'Шкільний Лайф': '\n150 грн на місяць\n7 ГБ інтернетy\nБезліміт на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
}

gadjet_descriptions = {
    'Ґаджет Безпека(Для датчиків руху та GPS/GSM-сигналізації)': '\n90 грн на місяць\n150 МБ інтернетy/на день\n15 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
    'Ґаджет Смарт(Для смарт-годинників)': '\n150 грн на місяць\n500 МБ інтернетy/на день\n50 смс/на день\n50 хв на lifecell/день\nБезліміт на lifecell після використання хвилин на всі номери',
    'Ґаджет Планшет(Для планшетів)': '\n275 грн на місяць\n50 ГБ інтернетy\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
    'Ґаджет Роутер(Для модемів та маршрутизаторів (роутерів))': '\n375 грн на місяць\nБезлімітний інтернет\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери',
} 

#bot commands
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.username}</b>"
    await message.answer(f"Привіт, {user_tag}! Я бот від Lifеcellbot тут ви можете оплатити тариф і тд ",
                         parse_mode='HTML')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)

#tarif choosing
@dp.message_handler(text='Обрати Тариф')
async def show_tariffs(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*tariff_buttons)
    await message.answer('Виберіть тариф:', reply_markup=keyboard)


@dp.message_handler(text=[tariff for tariff in tariff_descriptions.keys()])
async def show_tariff_description(message: types.Message):
    tariff = message.text
    description = tariff_descriptions.get(tariff)
    await message.answer(f'{tariff}: {description}')

#gadjet_types
@dp.message_handler(text='Ґаджет')
async def gadjet_types(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*gadjet_buttons)
    await message.answer('Виберіть тип тарифу:', reply_markup=keyboard)

@dp.message_handler(text=[gadjet for gadjet in gadjet_descriptions.keys()])
async def gadjet_description(message: types.Message):
    gadjet = message.text
    description = gadjet_descriptions.get(gadjet)
    await message.answer(f'{gadjet}: {description}')

#global funcs
@dp.message_handler(text='Назад')
async def go_back(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)


@dp.message_handler(text='Підтримка')
async def help(message: types.Message):
    url = 'https://www.lifecell.ua/uk/pidtrimka/'
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Перейти до підтримки', url=url))
    await message.answer('Якщо вам потрібна додаткова допомога, перейдіть за посиланням нижче:', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
