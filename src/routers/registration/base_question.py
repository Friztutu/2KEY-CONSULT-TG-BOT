from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from src.states import RegistrationState
from src.model import requests as rq
from src import strings


router = Router()


@router.callback_query(F.data == "Registration")
async def handle_marketplace_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text(strings.MARKETPLACE_QUESTION, reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.marketplace, F.data != "Main Menu")
async def handle_service_question(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = kb.SERVICE_QUESTION_INLINE_KEYBOARD_OZON

    if callback_query.data != "1":
        keyboard = kb.SERVICE_QUESTION_INLINE_KEYBOARD

    await state.update_data(marketplace=callback_query.data)
    await state.set_state(RegistrationState.service)
    await callback_query.message.edit_text(strings.SERVICE_QUESTION,reply_markup=keyboard)


@router.callback_query(RegistrationState.service, F.data != "Back")
async def handle_presence_market_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(service=callback_query.data)
    await state.set_state(RegistrationState.is_have_market)
    await callback_query.message.edit_text(strings.IS_HAVE_MARKET_QUESTION, reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.is_have_market, F.data == "2")
async def handle_problem_type_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(
        is_have_market=callback_query.data,
        market_duration=None,
        market_turnover=None,
        market_category=None,
        market_url=None,
    )

    data = await state.get_data()
    keyboard = kb.CLIENT_PROBLEM_INLINE_KEYBOARDS

    if data["is_have_market"] == "2" or data["service"] == "1":
        keyboard = kb.BACK_INLINE_KEYBOARD

    await state.set_state(RegistrationState.problem_type)
    await callback_query.message.edit_text(strings.PROBLEM_TYPE_QUESTION, reply_markup=keyboard)


@router.callback_query(RegistrationState.problem_type, F.data != "Back")
async def handle_callback_payment_type_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(problem_type=callback_query.data)

    data = await state.get_data()

    if data["service"] == "1":
        data["payment_method"] = None
        await rq.set_registered_user(callback_query.from_user.id, callback_query.from_user.first_name,
                                     callback_query.from_user.username, data)
        await state.clear()
        await callback_query.message.edit_text(strings.END_REGISTRATION_STRING)
    else:
        await state.set_state(RegistrationState.payment_method)
        await callback_query.message.edit_text(strings.PAYMENT_METHOD_QUESTION, reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)


@router.message(RegistrationState.problem_type)
async def handle_message_payment_type_question(message: types.Message, state: FSMContext):
    await state.update_data(problem_type=message.text)

    data = await state.get_data()

    if data["service"] == "1":
        data["payment_method"] = None
        await rq.set_registered_user(message.from_user.id, message.from_user.first_name,
                                     message.from_user.username, data)
        await state.clear()
        await message.answer(strings.END_REGISTRATION_STRING)
    else:
        await state.set_state(RegistrationState.payment_method)
        await message.answer(strings.PAYMENT_METHOD_QUESTION, reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.payment_method, F.data != "Back")
async def handle_callback_end_registration(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.update_data(payment_method=callback_query.data)
    data = await state.get_data()
    await rq.set_registered_user(callback_query.from_user.id, callback_query.from_user.first_name, callback_query.from_user.username, data)
    await state.clear()
    await callback_query.message.edit_text(strings.END_REGISTRATION_STRING)
