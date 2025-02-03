from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from .states import RegistrationState
from src.model import requests as rq
from src.basic_funcs import validation

router = Router()


@router.callback_query(RegistrationState.is_have_market, F.data == "Да")
async def handle_market_duration_question(callback_query: types.CallbackQuery, state: FSMContext):

    await state.update_data(is_have_market=callback_query.data)
    await state.set_state(RegistrationState.market_duration)
    await callback_query.message.edit_text("Сколько существует Ваш магазин?", reply_markup=kb.MARKET_DURATION_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_duration, F.data == "Back")
async def handle_market_duration_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.is_have_market)
    await callback_query.message.edit_text("У вас есть магазин?", reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_duration)
async def handle_market_turnover_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(market_duration=callback_query.data)
    await state.set_state(RegistrationState.market_turnover)
    await callback_query.message.edit_text("Ваш месячный оборот", reply_markup=kb.TURNOVER_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_turnover, F.data == "Back")
async def handle_market_turnover_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.market_duration)
    await callback_query.message.edit_text("Сколько существует Ваш магазин?", reply_markup=kb.MARKET_DURATION_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_turnover)
async def handle_market_category_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(market_turnover=callback_query.data)
    await state.set_state(RegistrationState.market_category)
    await callback_query.message.delete()
    await callback_query.message.answer("Категории, в которых работаете?", reply_markup=kb.BACK_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_category)
async def handle_market_category_question_back(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(RegistrationState.market_turnover)
    await callback_query.message.edit_text("Ваш месячный оборот", reply_markup=kb.TURNOVER_MARKET_INLINE_KEYBOARD)


@router.message(RegistrationState.market_category)
async def handle_market_url_question(message: types.Message, state: FSMContext):
    await state.update_data(market_category=message.text)
    await state.set_state(RegistrationState.market_url)
    await message.answer("Ссылка на ваш магазин?", reply_markup=kb.BACK_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_url)
async def handle_market_url_question_back(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(RegistrationState.market_category)
    await callback_query.message.edit_text("Категории, в которых работаете?", reply_markup=kb.BACK_INLINE_KEYBOARD)


@router.message(RegistrationState.market_url)
async def choice_payment_method_(message: types.Message, state: FSMContext):
    await state.update_data(market_url=message.text)

    data = await state.get_data()

    if data["service"] == "Разовая консультация":
        await state.update_data(payment_method=None)
        await state.set_state(RegistrationState.problem_type)
        await message.answer("Почему Вы решили обратиться к нам?", reply_markup=kb.CLIENT_PROBLEM_INLINE_KEYBOARDS)
    else:
        await state.set_state(RegistrationState.payment_method)
        await message.answer("Предпочтительный режим оплаты услуг менеджера", reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)
