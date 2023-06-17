from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Dispatcher, Bot, types, executor
import logging

# створюємо бота
BOT_TOKEN = Bot("6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo")
dp = Dispatcher(BOT_TOKEN) # створюємо диспетчер

# змінюємо рівень логінгу
logging.basicConfig(level=logging.INFO)

# створюємо кнопки головного меню 
main_menu_buttons = [
    KeyboardButton('🤔Обрати Тариф'),
    KeyboardButton('⚙️Створити свій тариф'),
    KeyboardButton('👩‍💻Підтримка'),
    KeyboardButton('🧑‍💻Розробники'),
    KeyboardButton('🇺🇦Патріотики')
]

# створюємо кнопки меню тарифів
tariff_buttons = [
    KeyboardButton('🤟Вільний Лайф'),
    KeyboardButton('✌️Смарт Лайф'),
    KeyboardButton('👍Просто Лайф'),
    KeyboardButton('🪙Platinum Лайф'),
    KeyboardButton('🏫Шкільний Лайф'),
    KeyboardButton('⌚️Ґаджет'),
    KeyboardButton('👨‍👩‍👦Смарт Сім\'я'),
    KeyboardButton('🔙Назад')
]

# створюємо кнопки тарифів Ґаджету
gadjet_buttons = [
    KeyboardButton('🔐Ґаджет Безпека'),
    KeyboardButton('⌚️Ґаджет Смарт'),
    KeyboardButton('📋Ґаджет Планшет'),
    KeyboardButton('🌐Ґаджет Роутер'),
    KeyboardButton('🔙Назад')
]

# створюємо кнопки тарифів Смарт Cім'я
family_buttons = [
    KeyboardButton('👫Смарт Сім\'я S'),
    KeyboardButton('👨‍👩‍👦Смарт Сім\'я M'),
    KeyboardButton('👨‍👩‍👧‍👦Смарт Сім\'я L'),
    KeyboardButton('🔙Назад')
]


# створюємо словник тарифів
tariff_descriptions = {
    '🤟Вільний Лайф': '\n180 грн на місяць\nБезлімітний інтернет\n1600 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/]',
    '✌️Смарт Лайф': '\n120 грн на місяць\n25 ГБ інтернету\n800 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/]',
    '👍Просто Лайф': '\n90 грн на місяць\n8 ГБ інтернету\n300 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/]',
    '🪙Platinum Лайф': '\n250 грн на місяць\nБезлімітний інтернет\n3000 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/]',
    '🏫Шкільний Лайф': '\n150 грн на місяць\n7 ГБ інтернету\nБезліміт на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/]',
    '🔐Ґаджет Безпека': '\n90 грн на місяць\n150 МБ інтернету/на день\n15 хв на всі номери по Україні (міські, мобільні, lifecell)\n\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/]',
    '⌚️Ґаджет Смарт': '\n150 грн на місяць\n500 МБ інтернету/на день\n50 смс/на день\n50 хв на lifecell/день\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/]',
    '📋Ґаджет Планшет': '\n275 грн на місяць\n50 ГБ інтернету\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/]',
    '🌐Ґаджет Роутер': '\n375 грн на місяць\nБезлімітний інтернет\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/]',
    '👫Смарт Сім\'я S': '\n375 грн на місяць\n20 ГБ інтернету\n500 хв на інші номери по Україні (міські, мобільні, lifecell)\n500 SMS на мобільні номери по Україні\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/]',
    '👨‍👩‍👦Смарт Сім\'я M': '\n425 грн на місяць\n30 ГБ інтернету\n750 хв на інші номери по Україні (міські, мобільні, lifecell)\n1000 SMS на мобільні номери по Україні\n\Переглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/]',
    '👨‍👩‍👧‍👦Смарт Сім\'я L': '\n500 грн на місяць\n50 ГБ інтернету\n1500 хв на інші номери по Україні (міські, мобільні, lifecell)\n1500 SMS на мобільні номери по Україні\n\nПереглянути/Придбати: [https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/]',
}


# створюємо усі функції з коммандами бота
# створюємо функцію для команди /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.full_name}</b>" # отримуємо повне ім'я користувача
    await message.answer(f"Привіт, {user_tag}! Я телеграм бот від Lifеcell тут ви можете обрати тариф, створити свій власний або звернутися до  підтримки 😉", parse_mode='HTML')
    # створюємо клавіатуру головного меню
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)

# створюємо функцію для команди /help
@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.full_name}</b>" # отримуємо повне ім'я користувача
    await message.answer(f"🫡 {user_tag}, я телеграм бот від Lifеcell, ваш помічник у виборі тарифу\n\n🤔 Натисніть Обрати тариф якщо ви хочете ознайомитися з нашими тарифами, та обрати найбільш підходящий для вас\n\n🤔 Натисніть Створити свій тариф, для того щоб зробити свій унікальний тариф із необхідними для вас функціями\n\n🤔 Натисніть Допомога якщо потребуєте допомоги наших операторів\n\n😘 Гарного користування ботом)", parse_mode='HTML')
    # створюємо клавіатуру головного меню
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*main_menu_buttons)
    await message.answer('Виберіть пункт:', reply_markup=keyboard)

# створюємо функцію для взаємодії з користувачем
@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    msg = message.text # отримуємо текст повідомлення користувача
    
    if msg == '🤔Обрати Тариф':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*tariff_buttons) # створюємо клавіатуру
        await message.answer('Виберіть тариф:', reply_markup=keyboard)

    elif msg in tariff_descriptions.keys():
        await message.answer(f'{msg}: {tariff_descriptions.get(msg)}')

    elif msg == '🔙Назад':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*main_menu_buttons) # створюємо клавіатуру
        await message.answer('Виберіть пункт:', reply_markup=keyboard)
    
    elif msg == '👩‍💻Підтримка':
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до підтримки', url='https://www.lifecell.ua/uk/pidtrimka/')) # створюємо клавіатуру
        await message.answer('Якщо вам потрібна додаткова допомога, перейдіть за посиланням нижче:', reply_markup=keyboard)

    elif msg == '⌚️Ґаджет':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*gadjet_buttons) # створюємо клавіатуру
        await message.answer('Виберіть тип тарифу:', reply_markup=keyboard)

    elif msg in tariff_descriptions.keys():
        await message.answer(f'{msg}: {tariff_descriptions.get(msg)}')

    elif msg == '👨‍👩‍👦Смарт Сім\'я':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*family_buttons) # створюємо клавіатуру
        await message.answer('Виберіть тип тарифу:', reply_markup=keyboard)

    elif msg in tariff_descriptions.keys():
        await message.answer(f'{msg}: {tariff_descriptions.get(msg)}')

    elif msg == '⚙️Створити свій тариф':
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до конструктора', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/')) # створюємо клавіатуру
        await message.answer('Ось посилання на наш сайт де ви зможете зробити власний, унікальний тариф:', reply_markup=keyboard)

    elif msg == '🇺🇦Патріотики':
        url='https://www.youtube.com/watch?v=noAUBPrNBxY'
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton('Відосик', url=url)) # створюємо клавіатуру
        await message.answer('Відосик з низу:', reply_markup=keyboard)

    elif msg == '🧑‍💻Розробники':
        developers_info = "Розробники програми:\n- @pristigio01m\n- @xedercat\n- @rxdxkk\n- @raysist1"
        await message.answer(developers_info)
# запускаємо бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
