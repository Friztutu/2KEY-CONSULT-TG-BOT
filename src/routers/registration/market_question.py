from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from .states import RegistrationState

router = Router()

@router.callback_query(RegistrationState.is_have_market, F.data == "Да")
async def choice_market_duration(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(is_have_market=callback_query.data)
    await state.set_state(RegistrationState.market_duration)
    await callback_query.message.edit_text("Сколько существует Ваш магазин?", reply_markup=kb.choice_duration_market)

@router.callback_query(RegistrationState.market_duration)
async def choice_market_turnover(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(market_duration=callback_query.data)
    await state.set_state(RegistrationState.market_turnover)
    await callback_query.message.edit_text("Ваш месячный оборот", reply_markup=kb.choice_turnover_market)

@router.callback_query(RegistrationState.market_turnover)
async def choice_market_category(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(market_turnover=callback_query.data)
    await state.set_state(RegistrationState.market_category)
    await callback_query.message.edit_text("Категории, в которых работаете")

@router.message(RegistrationState.market_category)
async def choice_url_market(message: types.Message, state: FSMContext):
    await state.update_data(market_category=message.text)
    await state.set_state(RegistrationState.market_url)
    await message.answer("Ссылка на ваш магазин")

@router.message(RegistrationState.market_url)
async def choice_payment_method_(message: types.Message, state: FSMContext):
    await state.update_data(market_url=message.text)
    await state.set_state(RegistrationState.payment_method)
    await message.answer("Предпочтительный режим оплаты услуг менеджера", reply_markup=kb.choice_payment_method)