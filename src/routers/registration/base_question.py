from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from .market_question import handle_market_url_question
from .states import RegistrationState
from src.model import requests as rq
from src.basic_funcs import validation

router = Router()

@router.callback_query(F.data == "Registration")
async def handle_marketplace_question(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text("Какой маркетплей вас интересует",
                                           reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.marketplace, F.data != "Main Menu")
async def handle_service_question(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.update_data(marketplace=callback_query.data)
    await state.set_state(RegistrationState.service)
    await callback_query.message.edit_text("Выберите необходимую услугу",
                                           reply_markup=kb.SERVICE_QUESTION_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.service, F.data == "Back")
async def handle_service_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text("Какой маркетплей вас интересует",
                                           reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.service, F.data != "Разовая консультация")
async def handle_presence_market_question(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.update_data(service=callback_query.data)
    await state.set_state(RegistrationState.is_have_market)
    await callback_query.message.edit_text("У вас есть магазин?",
                                           reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.is_have_market, F.data == "Back")
async def handle_presence_market_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.set_state(RegistrationState.service)
    await callback_query.message.edit_text("Выберите необходимую услугу",
                                           reply_markup=kb.SERVICE_QUESTION_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.is_have_market, F.data == "Нет")
async def handle_payment_method_question(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.update_data(
        is_have_market=callback_query.data,
        market_duration=None,
        market_turnover=None,
        market_category=None,
        market_url=None
    )
    await state.set_state(RegistrationState.payment_method)
    await callback_query.message.edit_text("Предпочтительный режим оплаты услуг менеджера",
                                           reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.payment_method, F.data == "Back")
async def handle_payment_method_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    data = await state.get_data()

    if "is_have_market" in data.keys():
        await state.set_state(RegistrationState.market_url)
        await callback_query.message.delete()
        await callback_query.message.answer("Ссылка на ваш магазин?",
                             reply_markup=kb.URL_MARKET_REPLAY_KEYBOARDS)
    else:
        await state.set_state(RegistrationState.is_have_market)
        await callback_query.message.edit_text("У вас есть магазин?",
                                               reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.payment_method)
async def handle_problem_type_question(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.update_data(payment_method=callback_query.data)
    await state.set_state(RegistrationState.problem_type)
    await callback_query.message.delete()
    await callback_query.message.answer("Почему Вы решили обратиться к Нам",
                                           reply_markup=kb.CLIENT_PROBLEM_REPLAY_KEYBOARDS)

@router.message(RegistrationState.problem_type, validation.is_back)
async def handle_problem_type_question_back(message: types.Message, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.set_state(RegistrationState.payment_method)
    await message.answer("Предпочтительный режим оплаты услуг менеджера",
                                           reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)

@router.message(RegistrationState.problem_type)
async def end_registration(message: types.Message, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.update_data(problem_type=message.text)
    data = await state.get_data()
    await rq.set_registered_user(message.from_user.id, message.from_user.first_name, data)
    await state.clear()
    await message.answer("Благодарим за то, что выбрали нас. Мы свяжемся с Вами в ближайшее время.")


