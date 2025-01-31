from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from .market_question import choice_url_market
from .states import RegistrationState
from src.model import requests as rq

router = Router()

@router.callback_query(F.data == "register")
async def choice_marketplace(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text("Какой маркетплей вас интересует", reply_markup=kb.choice_market_keyboard)

@router.callback_query(RegistrationState.marketplace, F.data != "start")
async def choice_service(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(marketplace=callback_query.data)
    await state.set_state(RegistrationState.service)

    keyboard = kb.choice_service_keyboard
    if callback_query.data == "Ozon":
        keyboard = kb.choice_ozon_service_keyboard

    await callback_query.message.edit_text("Выберите необходимую услугу", reply_markup=keyboard)

@router.callback_query(RegistrationState.service, F.data != "Разовая консультация")
async def choice_is_have_market(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(service=callback_query.data)
    await state.set_state(RegistrationState.is_have_market)
    await callback_query.message.edit_text("У вас есть магазин?", reply_markup=kb.choice_is_have_market)

@router.callback_query(RegistrationState.is_have_market, F.data == "Нет")
async def choice_payment_method(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(
        is_have_market=callback_query.data,
        market_duration=None,
        market_turnover=None,
        market_category=None,
        market_url=None
    )
    await state.set_state(RegistrationState.payment_method)
    await callback_query.message.edit_text("Предпочтительный режим оплаты услуг менеджера", reply_markup=kb.choice_payment_method)

@router.callback_query(RegistrationState.payment_method)
async def choice_problem_type(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(payment_method=callback_query.data)
    await state.set_state(RegistrationState.problem_type)
    await callback_query.message.edit_text("Почему Вы решили обратиться к Нам", reply_markup=kb.choice_problem)

@router.callback_query(RegistrationState.problem_type)
async def end_registration(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(problem_type=callback_query.data)
    data = await state.get_data()
    await rq.set_registered_user(callback_query.from_user.id, callback_query.from_user.first_name, data)
    await state.clear()
    await callback_query.message.edit_text("Благодарим за то, что выбрали нас. Мы свяжемся с Вами в ближайшее время.")