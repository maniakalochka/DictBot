from text_messages.text import *
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from repositories.user_repo import UserRepository


dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler_and_add_user(message: Message) -> None:
    repo = UserRepository()
    user_data = {
        "tg_id": message.from_user.id,
        "username": message.from_user.username,
    }
    user = await repo.create_user_if_does_not_exist(**user_data)

    await message.answer(START_CMD)
