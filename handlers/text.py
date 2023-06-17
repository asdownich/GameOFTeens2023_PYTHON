from aiogram import Dispatcher, types
from keyboards import kb
import config

async def text_f(message: types.Message):
    msg = message.text # отримуємо текст повідомлення користувача
    
    for tariff, data in config.tariff.items():
        if msg == tariff:
            if 'keyboard' in data:
                await message.answer(data['info'], reply_markup=data['keyboard'])
            else:
                await message.answer(data['info'])
        if msg in kb.internet:
            if 'internet' in data:
                if data['internet'] == msg:
                    d = data['info']
                    ans = f'{d}'
                    await message.answer(ans, reply_markup=data['keyboard'])
        if msg in kb.calls:
            if 'calls' in data:
                if data['calls'] == msg:
                    d = data['info']
                    ans = f'{d}'
                    await message.answer(ans, reply_markup=data['keyboard'])

    
    if msg == '⌚️Ґаджет':
        await message.answer('Виберіть тип тарифу:', reply_markup=kb.gadjet_kb)

    elif msg == '👨‍👩‍👦Смарт Сім\'я':
        await message.answer('Виберіть тип тарифу:', reply_markup=kb.family_kb)

def text(dp: Dispatcher):
    dp.register_message_handler(content_types=["text"], callback=text_f)
