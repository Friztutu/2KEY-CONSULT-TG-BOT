from aiogram.filters import Command, CommandStart
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from ..registration.states import RegistrationState

from src import keyboards as kb, strings
from src.model import requests as rq
from src.basic_funcs import helpers

router = Router(name=__name__)

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    await rq.set_user(message.from_user.id)
    await message.answer(f"Здравствуйте, {message.from_user.first_name}. " + strings.MAIN_MENU_STRING,
                         reply_markup=kb.MAIN_MENU_INLINE_KEYBOARD)


@router.message(Command("reg"))
async def cmb_choice_market(message: types.Message, state: FSMContext) -> None:
    await state.set_state(RegistrationState.marketplace)
    await message.answer("Какой маркетплей вас интересует",
                         reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)


@router.message(Command("about_ozon"))
async def cmb_about_ozon(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(strings.ABOUT_OZON_STRING,
                                           reply_markup=kb.ABOUT_US_INLINE_KEYBOARD)


@router.message(Command("about_wb"))
async def cmb_about_wb(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(strings.ABOUT_WB_STRING,
                                           reply_markup=kb.ABOUT_US_INLINE_KEYBOARD)


@router.message(Command("my_request"))
async def cmb_your_request(message: types.Message, state: FSMContext) -> None:
    await state.clear()

    user = await rq.get_registered_user_by_id(message.from_user.id)

    if user:
        await message.answer(helpers.registered_user_to_string(user))
    else:
        await message.answer(f"Вы еще не оставляли заявку 🥲")