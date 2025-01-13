from .base_kb import BaseReplyKeyboard


class LearnWordsKeyboard(BaseReplyKeyboard):
    def __init__(self) -> None:
        super().__init__()
        self.add_custom_button()

    def add_custom_button(self) -> None:
        self.add_button("👍")  # ответил правильно
        self.add_button("🔄")  # Сложно, надо на повтор
        self.add_button("❌")  # Не знаю
        self.add_button("🔙")  # назад в меню
