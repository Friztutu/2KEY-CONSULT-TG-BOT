from aiogram import types


def is_back(message: types.Message) -> bool:
    try:
        result = message.text.lower().strip() == "назад"
        return result
    except Exception:
        return False