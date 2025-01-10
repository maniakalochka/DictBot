from text_messages.text import *
from aiogram.filters import Command
from aiogram.types import Message
from extraction.reader import reader, filename
from ..keyboards.reply_keyboards.learn_word_kb import LearnWordKeyboard
from dispatcher import dp


@dp.message(Command("learn_words"))
async def command_random_handler(message: Message) -> None:
    random_word = await reader(filename)
    keyboard = LearnWordKeyboard()
    markup = keyboard.get_keyboard()
    await message.answer(random_word, reply_markup=markup)
