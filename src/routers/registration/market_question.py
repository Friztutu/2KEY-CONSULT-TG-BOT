from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

import src.keyboards as kb
from .states import RegistrationState
from src.model import requests as rq

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
    await callback_query.message.delete()
    await callback_query.message.answer("Категории, в которых работаете?", reply_markup=kb.categories_denied)

@router.message(RegistrationState.market_category)
async def choice_url_market(message: types.Message, state: FSMContext):
    await state.update_data(market_category=message.text)
    await state.set_state(RegistrationState.market_url)
    await message.answer("Ссылка на ваш магазин?", reply_markup=kb.url_market_denied)

@router.message(RegistrationState.market_url)
async def choice_payment_method_(message: types.Message, state: FSMContext):
    await state.update_data(market_url=message.text)

    data = await state.get_data()

    if data["service"] == "Разовая консультация":
        await state.update_data(
            payment_method=None,
            is_have_market=None,
            market_duration=None,
            market_turnover=None,
            market_category=None
        )
        data = await state.get_data()
        await rq.set_registered_user(message.from_user.id, message.from_user.first_name, data)
        await state.clear()
        await message.answer("Благодарим за то, что выбрали нас. Мы свяжемся с Вами в ближайшее время.")
    else:
        await state.set_state(RegistrationState.payment_method)
        await message.answer("Предпочтительный режим оплаты услуг менеджера", reply_markup=kb.choice_payment_method)
