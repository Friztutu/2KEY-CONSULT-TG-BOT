from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from io import StringIO

from src.basic_funcs.helpers import get_managers_id
from src.model import requests as rq
from config import ADMIN_USER_ID
from src import strings
from src.model.model import RegisteredUsers
from src.states import SendOneUserState
import csv


router = Router()


@router.message(Command("manager"))
async def handle_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    managers = await rq.get_all_managers()
    managers_id = get_managers_id(managers)

    if str(message.from_user.id) != str(ADMIN_USER_ID) and str(message.from_user.id) not in managers_id:
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await message.answer("Список доступных команд: \n"
                             "/table - Получить всех зарегистрированных пользователей\n"
                             "/send_to_user - Отправить одному пользователю сообщение\n")


@router.message(Command("table"))
async def handle_table_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    managers = await rq.get_all_managers()
    managers_id = get_managers_id(managers)

    if str(message.from_user.id) != str(ADMIN_USER_ID) and str(message.from_user.id) not in managers_id:
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        users: tuple[RegisteredUsers] = await rq.get_full_registered_users()

        csv_buffer = StringIO()
        writer = csv.writer(csv_buffer)

        # Заголовки
        writer.writerow([
            "Тг айди", "ТГ USERNAME", "Имя", "Маркетплейс", "Услуга", "Способ оплаты", "Проблема",
            "Наличие магазина", "Длительность магазина", "Оборот магазина", "Категории магазина", "Ссылка на магазин",
            "Время и Дата"

        ])

        # Данные
        for user in users:
            writer.writerow([
                user.tg_id, user.username, user.name, user.marketplace, user.service, user.payment_method,
                user.problem_type, user.is_have_market, user.market_duration, user.market_turnover,
                user.market_category, user.market_url, user.date
            ])

        # Подготавливаем файл для отправки
        csv_buffer.seek(0)
        csv_file = types.BufferedInputFile(
            csv_buffer.getvalue().encode(),
            filename="users_table.csv"
        )

        # Отправляем файл
        await message.answer_document(csv_file)


@router.message(Command("send_to_user"))
async def handle_send_to_user_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    managers = await rq.get_all_managers()
    managers_id = get_managers_id(managers)

    if str(message.from_user.id) != str(ADMIN_USER_ID) and str(message.from_user.id) not in managers_id:
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await state.set_state(SendOneUserState.tg_id)
        await message.answer("Напишите TG ID человека которому нужно отправить сообщение: ")


@router.message(SendOneUserState.tg_id)
async def handle_get_tg_id_user(message: types.Message, state: FSMContext) -> None:
    await state.update_data(tg_id=message.text)
    await state.set_state(SendOneUserState.message)
    await message.answer(f"Наберите сообщение которое нужно отправить пользователю (tg_id: {message.text}).")


@router.message(SendOneUserState.message)
async def handle_send_message_to_one_user(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.send_copy(chat_id=int(data["tg_id"]))
    await state.clear()
    await message.answer("Сообщение успешно отправлено.")
