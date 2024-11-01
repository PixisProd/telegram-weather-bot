from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_start_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text="☁ Get weather")
    kb.adjust(1)
    return kb.as_markup()