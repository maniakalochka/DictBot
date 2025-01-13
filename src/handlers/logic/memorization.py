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


@dp.message(Command("learn"))
async def get_random_word_from_db_handler(message: Message, state: FSMContext) -> None:
    repo = WordRepository()
    user_tg_id = message.from_user.id
    random_word = await repo.get_random_word(user_tg_id)
    keyboard = LearnWordsKeyboard()
    markup = keyboard.get_keyboard()
    translate = get_translation(iam_token, random_word.word)
    await state.update_data(random_word=random_word)
    await message.answer(
        text=f"{random_word}\n\n||{translate}||",
        parse_mode="MarkdownV2",
        reply_markup=markup,
    )
    await state.set_state(LearnWordsState.waiting_for_response)
