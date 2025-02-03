from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from src.model import requests as rq
from config import ADMIN_USER_ID
from src import strings
import csv

router = Router(name = __name__)

@router.message(Command("admin"))
async def handle_admin_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await message.answer("Список доступных команд: \n"
                             "/table - Получить всех зарегистрированных пользователей \n")


@router.message(Command("table"))
async def handle_table_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)


@router.message(Command("add_new_manager"))
async def handle_add_new_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await message.answer("Добавить нового админа")


@router.message(Command("send_all"))
async def handle_send_all_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await message.answer("Написать всем")


@router.message(Command("send_to_user"))
async def handle_send_to_user_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await message.answer("Написать конкретному типу")
