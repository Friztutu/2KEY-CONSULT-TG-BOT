from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from io import StringIO

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.model import requests as rq
from config import ADMIN_USER_ID
from src import strings
from src.model.model import RegisteredUsers
from src.states import NewManagerState, SendAllUserState, SendOneUserState, DeleteManagerState
import csv


CHUNK_SIZE = 1000

router = Router(name = __name__)


@router.message(Command("admin"))
async def handle_admin_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await message.answer("Список доступных команд: \n"
                             "/table - Получить всех зарегистрированных пользователей\n"
                             "/manager_list - Получить список всех менеджеров\n"
                             "/add_new_manager - Добавить нового менеджера\n"
                             "/delete_manager - Удалить старого менеджера\n"
                             "/send_to_user - Отправить одному пользователю сообщение\n"
                             "/send_all - Сделать общую рассылку\n")


@router.message(Command("manager_list"))
async def handle_manager_list_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        managers = await rq.get_all_managers()

        for manager in managers:
            await message.answer(f"Имя: {manager.first_name}, TG ID: {manager.tg_id}\n")


@router.message(Command("table"))
async def handle_table_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        users: tuple[RegisteredUsers] = await rq.get_full_registered_users()

        csv_buffer = StringIO()
        writer = csv.writer(csv_buffer)

        # Заголовки
        writer.writerow([
            "Тг айди", "Имя", "Маркетплейс", "Услуга", "Способ оплаты", "Проблема",
            "Наличие магазина", "Длительность магазина", "Оборот магазина", "Категории магазина", "Ссылка на магазин",
            "Teлефон"

        ])

        # Данные
        for user in users:
            writer.writerow([
                user.tg_id, user.name, user.marketplace, user.service, user.payment_method,
                user.problem_type, user.is_have_market, user.market_duration, user.market_turnover,
                user.market_category, user.market_url, user.phone
            ])

        # Подготавливаем файл для отправки
        csv_buffer.seek(0)
        csv_file = types.BufferedInputFile(
            csv_buffer.getvalue().encode(),
            filename="users_table.csv"
        )

        # Отправляем файл
        await message.answer_document(csv_file)


@router.message(Command("add_new_manager"))
async def handle_add_new_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await state.set_state(NewManagerState.first_name)
        await message.answer("Введите имя нового менеджера: ")


@router.message(NewManagerState.first_name)
async def handle_add_manager_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(first_name=message.text.strip())
    await state.set_state(NewManagerState.tg_id)
    await message.answer("Введите id нового менеджера: ")


@router.message(NewManagerState.tg_id)
async def handle_add_manager_id(message: types.Message, state: FSMContext) -> None:
    await state.update_data(tg_id=message.text.strip())
    data = await state.get_data()
    await message.answer(f"{data["tg_id"]}")
    await rq.set_new_manager(data)
    await state.clear()
    await message.answer("Новый менеджер добавлен.")


@router.message(Command("send_all"))
async def handle_send_all_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await state.set_state(SendAllUserState.message)
        await message.answer("Напишите сообщение которое хотите отправить: ")


@router.message(SendAllUserState.message)
async def handle_send_all(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    users = await rq.get_full_user()

    for user in users:
        await message.send_copy(chat_id=user.tg_id)


@router.message(Command("send_to_user"))
async def handle_send_to_user_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    if str(message.from_user.id) != str(ADMIN_USER_ID):
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


@router.message(Command("delete_manager"))
async def handle_delete_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.set_state(DeleteManagerState.tg_id)
    markup = InlineKeyboardBuilder()
    managers = await rq.get_all_managers()

    for manager in managers:
        markup.add(InlineKeyboardButton(text=f"Имя: {manager.first_name}, TG ID: {manager.tg_id}", callback_data=f"{manager.tg_id}"))

    await message.answer("Выберите менеджера которого надо удалить: ", reply_markup=markup.as_markup())


@router.callback_query(DeleteManagerState.tg_id)
async def handle_delete_manager(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    pass
