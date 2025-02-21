from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from src.states import RegistrationState
from src import strings

router = Router()


@router.callback_query(RegistrationState.is_have_market, F.data == "1")
async def handle_market_duration_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(is_have_market=callback_query.data)
    await state.set_state(RegistrationState.market_duration)
    await callback_query.message.edit_text(strings.MARKET_DURATION_QUESTION, reply_markup=kb.MARKET_DURATION_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_duration, F.data != "Back")
async def handle_market_turnover_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(market_duration=callback_query.data)
    await state.set_state(RegistrationState.market_turnover)
    await callback_query.message.edit_text(strings.MARKET_TURNOVER_QUESTION, reply_markup=kb.TURNOVER_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_turnover, F.data != "Back")
async def handle_market_category_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(market_turnover=callback_query.data)
    await state.set_state(RegistrationState.market_category)
    await callback_query.message.edit_text(strings.MARKET_CATEGORY_QUESTION, reply_markup=kb.BACK_INLINE_KEYBOARD)


@router.message(RegistrationState.market_category)
async def handle_market_url_question(message: types.Message, state: FSMContext):
    await state.update_data(market_category=message.text)
    await state.set_state(RegistrationState.market_url)
    await message.answer(strings.MARKET_URL_QUESTION, reply_markup=kb.BACK_INLINE_KEYBOARD)


@router.message(RegistrationState.market_url)
async def choice_payment_method_(message: types.Message, state: FSMContext):
    await state.update_data(market_url=message.text)
    await state.set_state(RegistrationState.problem_type)
    await message.answer(strings.PROBLEM_TYPE_QUESTION_WITH_VARIANTS, reply_markup=kb.CLIENT_PROBLEM_INLINE_KEYBOARDS)
