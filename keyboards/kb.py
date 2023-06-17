from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# створюємо кнопки головного меню 
main_menu_buttons = [
    KeyboardButton('🤔Обрати Тариф'),
    KeyboardButton('🔍Підібрати тариф'),
    KeyboardButton('⚙️Створити свій тариф'),
    KeyboardButton('👩‍💻Підтримка'),
    KeyboardButton('🧑‍💻Розробники'),
    KeyboardButton('🇺🇦')
]
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*main_menu_buttons)


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
tariff_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*tariff_buttons)

# створюємо кнопки тарифів Ґаджету
gadjet_buttons = [
    KeyboardButton('🔐Ґаджет Безпека'),
    KeyboardButton('⌚️Ґаджет Смарт'),
    KeyboardButton('📋Ґаджет Планшет'),
    KeyboardButton('🌐Ґаджет Роутер'),
    KeyboardButton('🔙Назад')
]
gadjet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*gadjet_buttons)

# створюємо кнопки тарифів Смарт Cім'я
family_buttons = [
    KeyboardButton('👫Смарт Сім\'я S'),
    KeyboardButton('👨‍👩‍👦Смарт Сім\'я M'),
    KeyboardButton('👨‍👩‍👧‍👦Смарт Сім\'я L'),
    KeyboardButton('🔙Назад')
]
family_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*family_buttons)

help_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до підтримки', url='https://www.lifecell.ua/uk/pidtrimka/'))
create_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Перейти до конструктора', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/'))
video_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Відосик', url='https://www.youtube.com/watch?v=noAUBPrNBxY'))

internet_calls_buttons = [
    KeyboardButton('Інтернет'),
    KeyboardButton('Хв на дзвінки'),
    KeyboardButton('🔙Назад')
]
internet_calls_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*internet_calls_buttons)

internet_buttons = [
    KeyboardButton('150 МБ/день'),
    KeyboardButton('500 МБ/день'),
    KeyboardButton('7 ГБ'),
    KeyboardButton('8 ГБ'),
    KeyboardButton('25 ГБ'),
    KeyboardButton('50 ГБ'),
    KeyboardButton('Безліміт.'),
    KeyboardButton('🔙Назад')
]
internet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*internet_buttons)

internet = [ '150 МБ/день', '500 МБ/день', '7 ГБ', '8 ГБ', '25 ГБ', '50 ГБ', 'Безліміт.' ]

calls_buttons = [
    KeyboardButton('0 хв'),
    KeyboardButton('15 хв'),
    KeyboardButton('50 хв/день'),
    KeyboardButton('300 хв'),
    KeyboardButton('500 хв'),
    KeyboardButton('750 хв'),
    KeyboardButton('800 хв'),
    KeyboardButton('1500 хв'),
    KeyboardButton('1600 хв'),
    KeyboardButton('3000 хв'),
    KeyboardButton('Безліміт'),
    KeyboardButton('🔙Назад')
]
calls_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*calls_buttons)

calls = [ '0 хв', '15 хв', '50 хв/день', '300 хв', '500 хв', '750 хв', '800 хв', '1500 хв', '1600 хв', '3000 хв', 'Безліміт' ]
