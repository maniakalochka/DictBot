from dispatcher import dp
from text.text import START_CMD
from aiogram.filters import Command
from repositories.user_repo import UserRepository
from aiogram.types import Message


@dp.message(Command("start"))
async def command_start_handler_and_add_user(message: Message) -> None:
    repo = UserRepository()
    user_data = {
        "tg_id": message.from_user.id,
        "username": message.from_user.username,
    }
    await repo.create_if_does_not_exist(**user_data)

    await message.answer(START_CMD)
