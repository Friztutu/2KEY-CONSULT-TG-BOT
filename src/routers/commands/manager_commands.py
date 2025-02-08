from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from datetime import datetime

from src.basic_funcs.helpers import get_csv_file
from src.basic_funcs.validation import is_date, is_manager
from src.model import requests as rq
from src import strings
from src.model.model import RegisteredUsers
from src.states import SendOneUserState, TableOneDayState


router = Router()


@router.message(Command("manager"), is_manager)
async def handle_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(strings.MANAGER_COMMANDS)


@router.message(Command("table"), is_manager)
async def handle_table_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    users: tuple[RegisteredUsers] = await rq.get_full_registered_users()

    if not users:
        await message.answer("В таблице нет записей")
    else:
        csv_file = get_csv_file(users)
        await message.answer_document(csv_file)


@router.message(Command("send_to_user"), is_manager)
async def handle_send_to_user_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(SendOneUserState.tg_id)
    await message.answer("Напишите TG ID человека которому нужно отправить сообщение: ")


@router.message(SendOneUserState.tg_id, is_manager)
async def handle_get_tg_id_user(message: types.Message, state: FSMContext) -> None:
    await state.update_data(tg_id=message.text)
    await state.set_state(SendOneUserState.message)
    await message.answer(f"Наберите сообщение которое нужно отправить пользователю (tg_id: {message.text}).")


@router.message(SendOneUserState.message, is_manager)
async def handle_send_message_to_one_user(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.send_copy(chat_id=int(data["tg_id"]))
    await state.clear()
    await message.answer("Сообщение успешно отправлено.")


@router.message(Command("table_one_day"), is_manager)
async def handle_table_one_day_command(message: types.Message, state: FSMContext) -> None:
    await state.set_state(TableOneDayState.date)
    await message.answer("Введите дату в формате: ГГГГ-ММ-ДД")


@router.message(TableOneDayState.date, is_date, is_manager)
async def handle_send_table_one_day(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    users = await rq.get_registered_users_by_day(datetime.strptime(message.text.strip(), "%Y-%m-%d").date())

    if not users:
        await message.answer("В таблице нет записей")
    else:
        csv_file = get_csv_file(users)
        await message.answer_document(csv_file)
