from text_messages.text import *
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(START_CMD)
