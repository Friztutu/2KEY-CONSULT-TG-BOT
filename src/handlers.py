from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

import src.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}. "
                         f"Мы команда 2KEY CONSULT -  эксперты по работе с маркетплейсами Wildberries, ОЗОН. "
                         f"У нас за плечами - 2 года успешной работы. \n"
                         f"Данный бот поможет Вам лучше узнать нас. \n"
                         f"Если бот не работает, напишите нам @key2consult ", reply_markup=kb.start_keyboard)

@router.callback_query(F.data == "start")
async def cmb_start_(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(f"Здравствуйте, {callback_query.message.from_user.first_name}. "
                         f"Мы команда 2KEY CONSULT -  эксперты по работе с маркетплейсами Wildberries, ОЗОН. "
                         f"У нас за плечами - 2 года успешной работы. \n"
                         f"Данный бот поможет Вам лучше узнать нас. \n"
                         f"Если бот не работает, напишите нам @key2consult ", reply_markup=kb.start_keyboard)

@router.callback_query(F.data == "About Wb")
async def cmd_about_wb(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Какой-то текст про WB", reply_markup=kb.about_wb_keyboard)

@router.callback_query(F.data == "About Ozon")
async def cmb_about_ozon(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Какой-то текст про Ozon", reply_markup=kb.about_ozon_keyboard)

@router.callback_query(F.data == "Achivements Ozon")
async def cmb_ozon_achivements(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Мы такие пиздатые на Ozon", reply_markup=kb.ozon_keyboard)

@router.callback_query(F.data == "Competencies Ozon")
async def cmb_ozon_competencies(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Мы такие компетентные на Ozon", reply_markup=kb.ozon_keyboard)

@router.callback_query(F.data == "Achivements Wb")
async def cmb_ozon_achivements(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Мы такие пиздатые на Wb", reply_markup=kb.wb_keyboard)

@router.callback_query(F.data == "Competencies Wb")
async def cmb_ozon_competencies(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Мы такие компетентные на Wb", reply_markup=kb.wb_keyboard)

@router.callback_query(F.data == "register")
async def cmb_choice_market(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Какой маркетплей вас интересует", reply_markup=kb.choice_market_keyboard)

@router.message(Command("reg"))
async def cmb_choice_market(message: types.Message):
    await message.answer("Какой маркетплей вас интересует", reply_markup=kb.choice_market_keyboard)

@router.message()
async def cmb_echo(message: types.Message):
    await message.answer("❌ Неизвестная команда\n"
                         "\n"
                         "/start - 🏠 Главная страница\n"
                         "/reg - 📌 Тарифы и стоимость\n"
                         "\n"
                         "Если возникли трудности, напишите нам @key2consult")
