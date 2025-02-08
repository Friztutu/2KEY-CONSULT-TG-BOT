from datetime import datetime, date
from aiogram import types
from src.model import requests as rq
from .helpers import get_managers_id
from config import ADMIN_USER_ID

async def is_back(message: types.Message) -> bool:
    try:
        result = message.text.lower().strip() == "назад"
        return result
    except Exception:
        return False


async def is_date(message: types.Message) -> bool | date:
    try:
        datetime.strptime(message.text.strip(), "%Y-%m-%d").date()
    except Exception:
        return False

    return True


async def is_manager(message: types.Message) -> bool:
    managers = await rq.get_all_managers()
    managers_id = get_managers_id(managers)
    return str(message.from_user.id) == str(ADMIN_USER_ID) or str(message.from_user.id) in managers_id


async def is_admin(message: types.Message) -> bool:
    return str(message.from_user.id) == str(ADMIN_USER_ID)