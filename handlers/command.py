from aiogram import Dispatcher, types
from keyboards import kb

# створюємо функцію для команди /start
async def start(message: types.Message):
    user_tag = f"<b>{message.from_user.full_name}</b>" # отримуємо повне ім'я користувача
    await message.answer(f"Привіт, {user_tag}! Я телеграм бот від Lifеcell тут ви можете обрати, підібрати або створити свій власний тариф чизвернутися до підтримки 😉",
        parse_mode='HTML',
        reply_markup=kb.main_menu_kb
    )
    

# створюємо функцію для команди /help
async def help(message: types.Message):
    user_tag = f"<b>{message.from_user.full_name}</b>" # отримуємо повне ім'я користувача
    await message.answer(f"🫡 {user_tag}, я телеграм бот від Lifеcell, ваш помічник у виборі тарифу\n\n🤔 Натисніть Обрати тариф якщо ви хочете ознайомитися з нашими тарифами, та обрати найбільш підходящий для вас\n\n🤔 Натисніть Підібрати тариф якщо ви хочете щоб ми допомогли вам обрати найбільш підходящий для вас тариф\n\n🤔 Натисніть Створити свій тариф, для того щоб зробити свій унікальний тариф із необхідними для вас функціями\n\n🤔 Натисніть Допомога якщо потребуєте допомоги наших операторів\n\n😘 Гарного користування ботом)",
        parse_mode='HTML',
        reply_markup=kb.main_menu_kb
    )


def command(dp: Dispatcher):
    dp.register_message_handler(commands=["start"], commands_prefix="!/", callback=start)
    dp.register_message_handler(commands=["help"], commands_prefix="!/", callback=help)
