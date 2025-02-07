from aiogram.filters import Command
from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.basic_funcs.helpers import get_managers_id
from src.model import requests as rq
from config import ADMIN_USER_ID
from src import strings
from src.states import NewManagerState, SendAllUserState, DeleteManagerState

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

        if not managers:
            await message.answer("Менеджеров нет")


@router.message(Command("add_new_manager"))
async def handle_add_new_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    managers = await rq.get_all_managers()
    managers_id = get_managers_id(managers)

    if str(message.from_user.id) != str(ADMIN_USER_ID) or message.from_user.id in managers_id:
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


@router.message(Command("delete_manager"))
async def handle_delete_manager_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    managers = await rq.get_all_managers()
    managers_id = get_managers_id(managers)

    if str(message.from_user.id) != str(ADMIN_USER_ID) or message.from_user.id in managers_id:
        await message.answer(strings.UNEXPECTED_COMMAND_STRING)
    else:
        await state.set_state(DeleteManagerState.tg_id)
        markup = InlineKeyboardBuilder()
        managers = await rq.get_all_managers()

        for manager in managers:
            markup.add(InlineKeyboardButton(text=f"Имя: {manager.first_name}, TG ID: {manager.tg_id}", callback_data=f"{manager.tg_id}"))

        await message.answer("Выберите менеджера которого надо удалить: ", reply_markup=markup.as_markup())


@router.callback_query(DeleteManagerState.tg_id)
async def handle_delete_manager(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await rq.delete_manager(int(callback_query.data))
    await callback_query.message.edit_text("Менеджер успешно удален")
