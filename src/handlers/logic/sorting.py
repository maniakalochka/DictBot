from ..dispatcher import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from extraction.reader import reader, filename
from keyboards.reply_keyboards.sort_words_kb import SortWordsKeyboard
from repositories.word_repo import WordRepository
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class SortWordsState(StatesGroup):
    waiting_for_response = State()


@dp.message(Command("learn_words"))
async def command_random_handler(message: Message, state: FSMContext) -> None:
    random_word_data = await reader(filename)
    keyboard = SortWordsKeyboard()
    markup = keyboard.get_keyboard()
    repo = WordRepository()
    tg_id = message.from_user.id
    random_word_data["tg_id"] = tg_id
    await repo.create_if_does_not_exist(**random_word_data)
    await state.update_data(random_word_data=random_word_data)
    await message.answer(text=random_word_data["word"], reply_markup=markup)
    await state.set_state(SortWordsState.waiting_for_response)


@dp.message(lambda message: message.text == "✅")
async def already_know_word_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    skipped_word = data.get("random_word_data")
    if skipped_word:
        repo = WordRepository()
        await repo.skip_word(word=skipped_word["word"])
        await message.answer("Скипнул слово.")

        random_word_data = await reader(filename)
        tg_id = message.from_user.id
        random_word_data["tg_id"] = tg_id
        await repo.create_if_does_not_exist(**random_word_data)
        await state.update_data(random_word_data=random_word_data)

        keyboard = SortWordsKeyboard()
        markup = keyboard.get_keyboard()
        await message.answer(text=random_word_data["word"], reply_markup=markup)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "➕")
async def add_word_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    new_word = data.get("random_word_data")
    if new_word:
        repo = WordRepository()
        await repo.create_if_does_not_exist(**new_word)
        await message.answer("Добавил в словарь.")

        random_word_data = await reader(filename)
        tg_id = message.from_user.id
        random_word_data["tg_id"] = tg_id
        await repo.create_if_does_not_exist(**random_word_data)
        await state.update_data(random_word_data=random_word_data)
        keyboard = SortWordsKeyboard()
        markup = keyboard.get_keyboard()
        await message.answer(text=random_word_data["word"], reply_markup=markup)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "🔄")
async def repeat_word_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    new_word = data.get("random_word_data")
    if new_word:
        repo = WordRepository()
        await repo.create_if_does_not_exist(**new_word)
        await message.answer("Добавил в словарь")

        random_word_data = await reader(filename)
        tg_id = message.from_user.id
        random_word_data["tg_id"] = tg_id
        await repo.create_if_does_not_exist(**random_word_data)
        await state.update_data(random_word_data=random_word_data)
        keyboard = SortWordsKeyboard()
        markup = keyboard.get_keyboard()
        await message.answer(text=random_word_data["word"], reply_markup=markup)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "🔙")
async def back_to_main_menu_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Возвращаю в главное меню.", reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()
