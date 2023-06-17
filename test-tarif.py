keyboard.add(KeyboardButton('Вільний Лайф \nПридбати: [тут посилання]'))
keyboard.add(KeyboardButton('Смарт Лайф \nПридбати: [тут посилання]'))
keyboard.add(KeyboardButton('Просто Лайф \nПридбати: [тут посилання]'))
keyboard.add(KeyboardButton('Platinum Лайф \nПридбати: [тут посилання]'))
keyboard.add(KeyboardButton('Шкільний Лайф \nПридбати: [тут посилання]'))
keyboard.add(KeyboardButton('Ґаджет \nПридбати: [тут посилання]'))
keyboard.add(KeyboardButton('Смарт Сімя \nПридбати: [тут посилання]'))


await bot.send_message(chat_id, 'Виберіть тарифний план:', reply_markup=keyboard)
