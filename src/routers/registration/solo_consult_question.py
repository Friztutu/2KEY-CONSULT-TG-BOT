from gc import callbacks

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from .states import RegistrationState
from src.model import requests as rq

router = Router()

@router.callback_query(RegistrationState.service, F.data == "Разовая консультация")
async def cmb_choice_problem(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(service=callback_query.data)
    await state.set_state(RegistrationState.problem_type)
    await callback_query.message.edit_text("Опишите вопрос, который вы хотите обсудить")

@router.message(RegistrationState.problem_type)
async def cmb_input_url(message: types.Message, state: FSMContext):
    await state.update_data(problem_type=message.text)
    await state.set_state(RegistrationState.market_url)
    await message.reply("Оставьте ссылку на ваш магазин.", reply_markup=kb.url_market_denied)
