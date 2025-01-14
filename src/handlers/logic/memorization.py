from ..dispatcher import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from extraction.reader import reader, filename
from keyboards.reply_keyboards.memorization_words_kb import LearnWordsKeyboard
from repositories.word_repo import WordRepository
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from repositories.word_repo import WordRepository
from api.translate import get_translation
from api.iam_token import iam_token


class LearnWordsState(StatesGroup):
    waiting_for_response = State()
    current_language = State()  # Состояние для отслеживания текущего языка


@dp.message(Command("learn"))
async def get_random_word_from_db_handler(message: Message, state: FSMContext) -> None:
    repo = WordRepository()
    user_tg_id = message.from_user.id
    random_eng_word = await repo.get_random_word(user_tg_id)

    if random_eng_word:
        # Установим начальный язык, если он не задан
        data = await state.get_data()
        if "current_language" not in data:
            await state.update_data(current_language="en")  # По умолчанию английский

        keyboard = LearnWordsKeyboard()
        markup = keyboard.get_keyboard()
        russian_word = get_translation(iam_token, random_eng_word.word)
        await state.update_data(random_word=random_eng_word)
        await message.answer(
            text=f"{random_eng_word}\n\n||{russian_word}||",
            parse_mode="MarkdownV2",
            reply_markup=markup,
        )
        await state.set_state(LearnWordsState.waiting_for_response)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "🇷🇺/🇬🇧")
async def change_language_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    current_language = data.get("current_language", "en")  # По умолчанию английский

    repo = WordRepository()
    user_tg_id = message.from_user.id
    random_eng_word = await repo.get_random_word(user_tg_id)

    if random_eng_word:
        # Меняем язык местами
        if current_language == "en":
            russian_word = get_translation(iam_token, random_eng_word.word)
            response_text = f"{russian_word}\n\n||{random_eng_word}||"
            new_language = "ru"
        else:
            russian_word = get_translation(iam_token, random_eng_word.word)
            response_text = f"{random_eng_word}\n\n||{russian_word}||"
            new_language = "en"

        keyboard = LearnWordsKeyboard()
        markup = keyboard.get_keyboard()
        await state.update_data(
            random_word=random_eng_word, current_language=new_language
        )
        await message.answer(
            text=response_text,
            parse_mode="MarkdownV2",
            reply_markup=markup,
        )
        await state.set_state(LearnWordsState.waiting_for_response)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "👍")
async def continue_learning_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    current_language = data.get("current_language", "en")  # По умолчанию английский

    repo = WordRepository()
    user_tg_id = message.from_user.id
    current_word = data["random_word"]
    await repo.update_count(current_word.word)
    random_eng_word = await repo.get_random_word(user_tg_id)

    if random_eng_word:
        keyboard = LearnWordsKeyboard()
        markup = keyboard.get_keyboard()

        if current_language == "en":
            russian_word = get_translation(iam_token, random_eng_word.word)
            response_text = f"{random_eng_word}\n\n||{russian_word}||"
        else:
            russian_word = get_translation(iam_token, random_eng_word.word)
            response_text = f"{russian_word}\n\n||{random_eng_word}||"

        await state.update_data(random_word=random_eng_word)
        await message.answer(
            text=response_text,
            parse_mode="MarkdownV2",
            reply_markup=markup,
        )
        await state.set_state(LearnWordsState.waiting_for_response)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "❌")
async def continue_learning_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    current_language = data.get("current_language", "en")  # По умолчанию английский

    repo = WordRepository()
    user_tg_id = message.from_user.id
    random_eng_word = await repo.get_random_word(user_tg_id)

    if random_eng_word:
        keyboard = LearnWordsKeyboard()
        markup = keyboard.get_keyboard()

        if current_language == "en":
            russian_word = get_translation(iam_token, random_eng_word.word)
            response_text = f"{random_eng_word}\n\n||{russian_word}||"
        else:
            russian_word = get_translation(iam_token, random_eng_word.word)
            response_text = f"{russian_word}\n\n||{random_eng_word}||"

        await state.update_data(random_word=random_eng_word)
        await message.answer(
            text=response_text,
            parse_mode="MarkdownV2",
            reply_markup=markup,
        )
        await state.set_state(LearnWordsState.waiting_for_response)
    else:
        await message.answer("Слово не найдено.")


@dp.message(lambda message: message.text == "🔙")
async def back_to_main_menu_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Возвращаю в главное меню.", reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()
