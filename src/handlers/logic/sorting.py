from dispatcher import dp
from aiogram.types import Message
from aiogram.filters import Command
from extraction.reader import reader, filename
from keyboards.reply_keyboards.learn_word_kb import LearnWordKeyboard


@dp.message(Command("learn_words"))
async def command_random_handler(message: Message) -> None:
    random_word = await reader(filename)
    keyboard = LearnWordKeyboard()
    markup = keyboard.get_keyboard()
    await message.answer(text=random_word, reply_markup=markup)


@dp.message(lambda message: message.text == "✅")
async def already_know_word_handler(message: Message) -> None:
    await message.answer("Добавлено в изученные слова")
