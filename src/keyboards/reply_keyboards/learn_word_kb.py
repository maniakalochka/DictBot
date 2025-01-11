from .base_kb import BaseReplyKeyboard


class LearnWordKeyboard(BaseReplyKeyboard):
    def __init__(self) -> None:
        super().__init__()
        self.add_custom_button()

    def add_custom_button(self) -> None:
        self.add_button("✅")
        self.add_button("🔄")
        self.add_button("❌")
        self.add_button("🔙")
