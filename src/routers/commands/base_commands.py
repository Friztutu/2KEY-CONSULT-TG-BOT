from aiogram.filters import Command, CommandStart
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from ..registration.states import RegistrationState

from src import keyboards as kb, config
from src.model import requests as rq

router = Router(name=__name__)

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    types.ReplyKeyboardRemove()
    await rq.set_user(message.from_user.id)
    await message.answer(f"Здравствуйте, {message.from_user.first_name}. " + config.MAIN_MENU_STRING, reply_markup=kb.start_keyboard)

@router.message(Command("reg"))
async def cmb_choice_market(message: types.Message, state: FSMContext):
    types.ReplyKeyboardRemove()
    await state.set_state(RegistrationState.marketplace)
    await message.answer("Какой маркетплей вас интересует", reply_markup=kb.choice_market_keyboard)