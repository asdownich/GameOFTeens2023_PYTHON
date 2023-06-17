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
        KeyboardButton('7 ГБ'),
        KeyboardButton('8 ГБ'),
        KeyboardButton('25 ГБ'),
        KeyboardButton('Безліміт')
    )
    return markup
def calls():
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton('300 хв'),
        KeyboardButton('800 хв'),
        KeyboardButton('1600 хв'),
        KeyboardButton('3000 хв'),
        KeyboardButton('Безліміт')
    )
    return markup
