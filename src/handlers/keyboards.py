from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


class BaseKeyboard:

    def __init__(self):
        self.builder = ReplyKeyboardBuilder()

    def add_button(self, label: str) -> None:
        self.builder.add(KeyboardButton(text=label))

    def get_keyboard(self) -> ReplyKeyboardBuilder:
        return self.builder.as_markup(resize_keyboard=True)


class LearnWordKeyboard(BaseKeyboard):

    def __init__(self) -> None:
        super().__init__()
        self.add_custom_button()

    def add_custom_button(self) -> None:
        self.add_button("✅")
        self.add_button("🔄")
        self.add_button("❌")
        self.add_button("🔙")
