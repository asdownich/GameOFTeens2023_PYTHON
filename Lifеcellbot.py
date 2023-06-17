#сделать ссылку на покупку тарифов под их описаниями
#сделать конструктор тарифа по примеру с сайта: https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/
#косметическая доработка бота(кнопки назад, текст)
#проверка, при необходимости доработка
#запись екрана с работой бота
#собрать всё в файл на гитхабе и мы полностью готовы
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher, Bot, types, executor
import logging

#6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo
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
    KeyboardButton('Смарт Сім\'я'),
    KeyboardButton('Назад')
]

gadjet_buttons = [
    KeyboardButton('Ґаджет Безпека'),
    KeyboardButton('Ґаджет Смарт'),
    KeyboardButton('Ґаджет Планшет'),
    KeyboardButton('Ґаджет Роутер'),
    KeyboardButton('Назад')
]

family_buttons = [
    KeyboardButton('Смарт Сім\'я S'),
    KeyboardButton('Смарт Сім\'я M'),
    KeyboardButton('Смарт Сім\'я L'),
    KeyboardButton('Назад')
]

tariff_descriptions = {
    'Вільний Лайф': '\n180 грн на місяць\nБезлімітний інтернет\n1600 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/]',
    'Смарт Лайф': '\n120 грн на місяць\n25 ГБ інтернету\n800 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/]',
    'Просто Лайф': '\n90 грн на місяць\n8 ГБ інтернету\n300 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/]',
    'Platinum Лайф': '\n250 грн на місяць\nБезлімітний інтернет\n3000 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/]',
    'Шкільний Лайф': '\n150 грн на місяць\n7 ГБ інтернету\nБезліміт на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/]',
}

gadget_descriptions = {
    'Ґаджет Безпека': '\n90 грн на місяць\n150 МБ інтернету/на день\n15 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/]',
    'Ґаджет Смарт': '\n150 грн на місяць\n500 МБ інтернету/на день\n50 смс/на день\n50 хв на lifecell/день\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/]',
    'Ґаджет Планшет': '\n275 грн на місяць\n50 ГБ інтернету\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/]',
    'Ґаджет Роутер': '\n375 грн на місяць\nБезлімітний інтернет\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/]',
}

family_descriptions = {
    'Смарт Сім\'я S': '\n375 грн на місяць\n20 ГБ інтернету\n500 хв на інші номери по Україні (міські, мобільні, lifecell)\n500 SMS на мобільні номери по Україні\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/]',
    'Смарт Сім\'я M': '\n425 грн на місяць\n30 ГБ інтернету\n750 хв на інші номери по Україні (міські, мобільні, lifecell)\n1000 SMS на мобільні номери по Україні\n\Переглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/]',
    'Смарт Сім\'я L': '\n500 грн на місяць\n50 ГБ інтернету\n1500 хв на інші номери по Україні (міські, мобільні, lifecell)\n1500 SMS на мобільні номери по Україні\n\nПереглянути/купити: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/]',
}

#bot commands
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.full_name}</b>"
    await message.answer(f"Привіт, {user_tag}! Я бот від Lifеcellbot тут ви можете обрати тариф, створити свій власний або звернутися до  підтримки 😉",
                         parse_mode='HTML')

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    msg = message.text

    if msg == 'Обрати Тариф':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*tariff_buttons)
        await message.answer('Виберіть тариф:', reply_markup=keyboard)

    elif msg in tariff_descriptions.keys():
        await message.answer(f'{msg}: {tariff_descriptions.get(msg)}')

    elif msg == 'Допомога':
        url = 'https://www.lifecell.ua/uk/pidtrimka/'
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до підтримки', url=url))
        await message.answer('Якщо вам потрібна додаткова допомога, перейдіть за посиланням нижче:', reply_markup=keyboard)

    elif msg == 'Назад':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*main_menu_buttons)
        await message.answer('Виберіть пункт:', reply_markup=keyboard)
    
    elif msg == 'Підтримка':
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до підтримки', url='https://www.lifecell.ua/uk/pidtrimka/'))
        await message.answer('Якщо вам потрібна додаткова допомога, перейдіть за посиланням нижче:', reply_markup=keyboard)

    elif msg == 'Ґаджет':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*gadjet_buttons)
        await message.answer('Виберіть тип тарифу:', reply_markup=keyboard)

    elif msg in gadjet_descriptions.keys():
        await message.answer(f'{msg}: {gadjet_descriptions.get(msg)}')

    elif msg == 'Смарт Сім\'я':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*family_buttons)
        await message.answer('Виберіть тип тарифу:', reply_markup=keyboard)

    elif msg in family_descriptions.keys():
        await message.answer(f'{msg}: {family_descriptions.get(msg)}')

    elif msg == 'Створити свій тариф':
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до конструктора', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/'))
        await message.answer('Ось посилання на наш сайт де ви зможете зробити власний, унікальний тариф:', reply_markup=keyboard)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
