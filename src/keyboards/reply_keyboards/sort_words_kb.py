from .base_kb import BaseReplyKeyboard


class SortWordsKeyboard(BaseReplyKeyboard):
    def __init__(self) -> None:
        super().__init__()
        self.add_custom_button()

    def add_custom_button(self) -> None:
        self.add_button("✅")  # Знает слово
        self.add_button("🔄")  # Хотел бы отправить на повтор
        self.add_button("➕")  # Добавить в словарь
        self.add_button("🔙")  # Назад в меню
