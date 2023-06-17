from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# створюємо кнопки головного меню 
main_menu_buttons = [
    KeyboardButton('🤔Обрати Тариф'),
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