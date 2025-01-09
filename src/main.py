import asyncio
import logging
import sys

from aiogram import Bot
from core.config import settings
from handlers.handlers import *
from database.db import init_db


TOKEN = settings.TELEGRAM_TOKEN


async def main() -> None:
    bot = Bot(token=TOKEN)
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
