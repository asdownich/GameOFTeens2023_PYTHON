API_TOKEN = "6056717794:AAE8KjnkQXAQkDrXScqfUVX6Vmi4q1hP9mo"
from keyboards import kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tariff = {
    '🤟Вільний Лайф': {
        'info': '\n180 грн на місяць\nБезлімітний інтернет\n1600 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\n',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/'))
    },
    '✌️Смарт Лайф': {
        'info': '\n120 грн на місяць\n25 ГБ інтернету\n800 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/'))
    },
    '👍Просто Лайф': {
        'info': '\n90 грн на місяць\n8 ГБ інтернету\n300 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/'))
    },
    '🪙Platinum Лайф': {
        'info': '\n250 грн на місяць\nБезлімітний інтернет\n3000 хв на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/'))
    },
    '🏫Шкільний Лайф': {
        'info': '\n150 грн на місяць\n7 ГБ інтернету\nБезліміт на всі номери по Україні (міські, мобільні, lifecell)\nБезліміт на lifecell після використання хвилин на всі номери\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/'))
    },
    '🔐Ґаджет Безпека': {
        'info': '\n90 грн на місяць\n150 МБ інтернету/на день\n15 хв на всі номери по Україні (міські, мобільні, lifecell)\n\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/'))
    },
    '⌚️Ґаджет Смарт': {
        'info': '\n150 грн на місяць\n500 МБ інтернету/на день\n50 смс/на день\n50 хв на lifecell/день\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/'))
    },
    '📋Ґаджет Планшет': {
        'info': '\n275 грн на місяць\n50 ГБ інтернету\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart21/'))
    },
    '🌐Ґаджет Роутер': {
        'info':  '\n375 грн на місяць\nБезлімітний інтернет\n0 хв на всі номери по Україні (міські, мобільні, lifecell)\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-rout21/'))
    },
    '👫Смарт Сім\'я S': {
        'info': '\n375 грн на місяць\n20 ГБ інтернету\n500 хв на інші номери по Україні (міські, мобільні, lifecell)\n500 SMS на мобільні номери по Україні\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-s/'))
    },
    '👨‍👩‍👦Смарт Сім\'я M': {
        'info': '\n425 грн на місяць\n30 ГБ інтернету\n750 хв на інші номери по Україні (міські, мобільні, lifecell)\n1000 SMS на мобільні номери по Україні\n\Переглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart_simja-m/'))
    },
    '👨‍👩‍👧‍👦Смарт Сім\'я L': {
        'info': '\n500 грн на місяць\n50 ГБ інтернету\n1500 хв на інші номери по Україні (міські, мобільні, lifecell)\n1500 SMS на мобільні номери по Україні\n\nПереглянути/Придбати:',
        'keyboard': InlineKeyboardMarkup().add(InlineKeyboardButton('Переглянути/Придбати', url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-family-l/'))
    },
    '🤔Обрати Тариф': {
        'info': 'Виберіть тариф:',
        'keyboard': kb.tariff_kb
    },
    '🔙Назад': {
        'info': 'Виберіть пункт:',
        'keyboard': kb.main_menu_kb
    },
    '👩‍💻Підтримка': {
        'info': 'Якщо вам потрібна додаткова допомога, перейдіть за посиланням нижче:',
        'keyboard': kb.help_kb
    },
    '⚙️Створити свій тариф': {
        'info': 'Ось посилання на наш сайт де ви зможете зробити власний, унікальний тариф:',
        'keyboard': kb.create_kb
    },
    '🇺🇦': {
        'info': 'Відосик з низу:',
        'keyboard': kb.video_kb
    },
    '🧑‍💻Розробники': {
        'info': "Розробники програми:\n- @pristigio01m\n- @xedercat\n- @rxdxkk\n- @raysist1"
    }
}