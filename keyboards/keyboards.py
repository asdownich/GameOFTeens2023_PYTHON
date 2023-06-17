from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
def user():
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton('Для себе'),
        KeyboardButton('Для Ґаджету'),
        KeyboardButton('Для усієї сім\'ї')
    )
    return markup
def internet():
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton('150 МБ/день'),
        KeyboardButton('500 МБ/день'),
        KeyboardButton('7 ГБ'),
        KeyboardButton('8 ГБ'),
        KeyboardButton('25 ГБ'),
        KeyboardButton('50 ГБ'),
        KeyboardButton('Безліміт')
    )
    return markup
def calls():
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
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
        KeyboardButton('Безліміт')
    )
    return markup
