from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


class BaseReplyKeyboard:
    def __init__(self) -> None:
        self.builder = ReplyKeyboardBuilder()

    def add_button(self, label: str) -> None:
        self.builder.add(KeyboardButton(text=label))

    def get_keyboard(self) -> ReplyKeyboardBuilder:
        return self.builder.as_markup(resize_keyboard=True)
