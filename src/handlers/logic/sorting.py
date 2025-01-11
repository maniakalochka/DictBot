from ..dispatcher import dp
from aiogram.types import Message
from aiogram.filters import Command
from extraction.reader import reader, filename
from keyboards.reply_keyboards.learn_word_kb import LearnWordKeyboard
from repositories.word_repo import WordRepository
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class LearnWordsState(StatesGroup):
    waiting_for_response = State()


@dp.message(Command("learn_words"))
async def command_random_handler(message: Message, state: FSMContext) -> None:
    random_word_data = await reader(filename)
    keyboard = LearnWordKeyboard()
    markup = keyboard.get_keyboard()
    repo = WordRepository()
    tg_id = message.from_user.id
    random_word_data["tg_id"] = tg_id
    await repo.create_if_does_not_exist(**random_word_data)
    await state.update_data(random_word_data=random_word_data)
    await message.answer(text=random_word_data["word"], reply_markup=markup)
    await state.set_state(LearnWordsState.waiting_for_response)


@dp.message(lambda message: message.text == "✅")
async def already_know_word_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    skipped_word = data.get("random_word_data")
    if skipped_word:
        repo = WordRepository()
        await repo.skip_word(word=skipped_word["word"])
        await message.answer("Скипнул слово.")
        await state.clear()
    else:
        await message.answer("Слово не найдено.")
