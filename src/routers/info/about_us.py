from aiogram import Router, types, F
import src.keyboards as kb
from src import config

router = Router()

@router.callback_query(F.data == "start")
async def cmb_start_(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text(
        f"Здравствуйте, {callback_query.message.from_user.first_name}. " + config.MAIN_MENU_STRING, reply_markup=kb.start_keyboard)

@router.callback_query(F.data == "About Wb")
async def cmd_about_wb(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text("Какой-то текст про WB", reply_markup=kb.about_wb_keyboard)

@router.callback_query(F.data == "About Ozon")
async def cmb_about_ozon(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text("Какой-то текст про Ozon", reply_markup=kb.about_ozon_keyboard)

@router.callback_query(F.data == "Achivements Ozon")
async def cmb_ozon_achivements(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text("Мы такие пиздатые на Ozon", reply_markup=kb.ozon_keyboard)

@router.callback_query(F.data == "Competencies Ozon")
async def cmb_ozon_competencies(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text("Мы такие компетентные на Ozon", reply_markup=kb.ozon_keyboard)

@router.callback_query(F.data == "Achivements Wb")
async def cmb_ozon_achivements(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text("Мы такие пиздатые на Wb", reply_markup=kb.wb_keyboard)

@router.callback_query(F.data == "Competencies Wb")
async def cmb_ozon_competencies(callback_query: types.CallbackQuery):
    types.ReplyKeyboardRemove()
    await callback_query.message.edit_text("Мы такие компетентные на Wb", reply_markup=kb.wb_keyboard)

@router.message()
async def cmb_echo(message: types.Message):
    await message.answer(config.UNEXPECTED_COMMAND_STRING)