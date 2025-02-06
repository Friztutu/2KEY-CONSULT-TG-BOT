from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from src.states import RegistrationState
from src.model import requests as rq


router = Router()


@router.callback_query(F.data == "Registration")
async def handle_marketplace_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text("Какой маркетплей вас интересует?",
                                           reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)

@router.callback_query(RegistrationState.marketplace, F.data != "Main Menu")
async def handle_service_question(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = kb.SERVICE_QUESTION_INLINE_KEYBOARD_OZON

    if callback_query.data != "1":
        keyboard = kb.SERVICE_QUESTION_INLINE_KEYBOARD

    await state.update_data(marketplace=callback_query.data)
    await state.set_state(RegistrationState.service)
    await callback_query.message.edit_text("Выберите необходимую услугу:",reply_markup=keyboard)


@router.callback_query(RegistrationState.service, F.data != "Back")
async def handle_presence_market_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(service=callback_query.data)
    await state.set_state(RegistrationState.is_have_market)
    await callback_query.message.edit_text("У вас есть магазин?",
                                           reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.is_have_market, F.data == "2")
async def handle_payment_method_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(
        is_have_market=callback_query.data,
        market_duration=None,
        market_turnover=None,
        market_category=None,
        market_url=None,
    )

    data = await state.get_data()

    if data["service"] == "Разовая консультация":
        await state.update_data(payment_method=None)
        await state.set_state(RegistrationState.problem_type)
        await callback_query.message.delete()
        await callback_query.message.answer("Почему Вы решили обратиться к нам?",
                                            reply_markup=kb.CLIENT_PROBLEM_INLINE_KEYBOARDS)
    else:
        await state.set_state(RegistrationState.payment_method)
        await callback_query.message.edit_text("Предпочтительный режим оплаты услуг менеджера?",
                                               reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.payment_method, F.data != "Back")
async def handle_problem_type_question(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(payment_method=callback_query.data)
    await state.set_state(RegistrationState.problem_type)
    await callback_query.message.delete()
    await callback_query.message.answer("Почему Вы решили обратиться к нам?", reply_markup=kb.CLIENT_PROBLEM_INLINE_KEYBOARDS)


@router.callback_query(RegistrationState.problem_type, F.data != "Back")
async def handle_request_contact(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.update_data(problem_type=callback_query.data)
    await state.set_state(RegistrationState.contact)
    await callback_query.message.delete()
    await callback_query.message.answer("Ваши контакты для связи?", reply_markup=kb.REQUEST_CONTACT_INLINE_KEYBOARD)


@router.message(RegistrationState.contact)
async def end_registration(message: types.Message, state: FSMContext):
    if message.contact is not None:
        await state.update_data(contact=message.contact.phone_number)
        data = await state.get_data()
        await rq.set_registered_user(message.from_user.id, message.from_user.first_name, data)
        await state.clear()
        await message.answer("Благодарим за то, что выбрали нас. Мы свяжемся с Вами в ближайшее время.", reply_markup=types.ReplyKeyboardRemove())
    else:
        await state.update_data(contact=message.text)
        data = await state.get_data()
        await rq.set_registered_user(message.from_user.id, message.from_user.first_name, data)
        await state.clear()
        await message.answer("Благодарим за то, что выбрали нас. Мы свяжемся с Вами в ближайшее время.",
                             reply_markup=types.ReplyKeyboardRemove())



