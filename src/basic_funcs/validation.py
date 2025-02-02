from aiogram import types


def is_back(message: types.Message) -> bool:
    return message.text.lower().strip() == "назад"