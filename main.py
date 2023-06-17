from aiogram import Dispatcher, Bot, types, executor
import logging
import config

from keyboards import kb

from handlers.command import command
from handlers.text import text

bot = Bot(config.API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


def __register_handlers(dp) -> None:
    command(dp)
    text(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=__register_handlers(dp))
    