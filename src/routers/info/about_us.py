from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from src import strings

router = Router()

@router.callback_query(F.data == "Main Menu")
async def cmb_start_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.edit_text(
        f"Здравствуйте, {callback_query.message.from_user.first_name}. " + strings.MAIN_MENU_STRING,
        reply_markup=kb.MAIN_MENU_INLINE_KEYBOARD)

@router.callback_query(F.data == "About WB")
async def cmd_about_wb(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.edit_text(strings.ABOUT_WB_STRING,
                                           reply_markup=kb.ABOUT_US_INLINE_KEYBOARD)

@router.callback_query(F.data == "About Ozon")
async def cmb_about_ozon(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.edit_text(strings.ABOUT_OZON_STRING,
                                           reply_markup=kb.ABOUT_US_INLINE_KEYBOARD)

@router.message()
async def cmb_echo(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(strings.UNEXPECTED_COMMAND_STRING)