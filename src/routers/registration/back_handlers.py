from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram import Router

from src import keyboards as kb
from src.basic_funcs.validation import is_back
from src.states import RegistrationState
from src import strings


router = Router(name=__name__)

@router.callback_query(RegistrationState.service, F.data == "Back")
async def handle_service_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text(strings.MARKETPLACE_QUESTION, reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.is_have_market, F.data == "Back")
async def handle_presence_market_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.service)
    data = await state.get_data()
    keyboard = kb.SERVICE_QUESTION_INLINE_KEYBOARD_OZON

    if data["marketplace"] != "1":
        keyboard = kb.SERVICE_QUESTION_INLINE_KEYBOARD

    await callback_query.message.edit_text(strings.SERVICE_QUESTION, reply_markup=keyboard)


@router.callback_query(RegistrationState.problem_type, F.data == "Back")
async def handle_problem_type_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    if data["is_have_market"] == "1":
        await state.set_state(RegistrationState.market_url)
        await callback_query.message.delete()
        await callback_query.message.answer(strings.MARKET_URL_QUESTION, reply_markup=kb.BACK_INLINE_KEYBOARD)
    else:
        await state.set_state(RegistrationState.is_have_market)
        await callback_query.message.edit_text(strings.IS_HAVE_MARKET_QUESTION, reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.payment_method, F.data == "Back")
async def handle_payment_method_question_back(callback_query: types.CallbackQuery, state: FSMContext):
     await state.set_state(RegistrationState.problem_type)

     data = await state.get_data()
     keyboard = kb.CLIENT_PROBLEM_INLINE_KEYBOARDS
     message_text = strings.PROBLEM_TYPE_QUESTION_WITH_VARIANTS

     if data["is_have_market"] == "2" or data["service"] == "1":
         keyboard = kb.BACK_INLINE_KEYBOARD
         message_text = strings.PROBLEM_TYPE_QUESTION_WITHOUT_VARIANTS

     await callback_query.message.edit_text(message_text, reply_markup=keyboard)


@router.callback_query(RegistrationState.market_duration, F.data == "Back")
async def handle_market_duration_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.is_have_market)
    await callback_query.message.edit_text(strings.IS_HAVE_MARKET_QUESTION, reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_turnover, F.data == "Back")
async def handle_market_turnover_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationState.market_duration)
    await callback_query.message.edit_text(strings.MARKET_DURATION_QUESTION, reply_markup=kb.MARKET_DURATION_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_category)
async def handle_market_category_question_back(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(RegistrationState.market_turnover)
    await callback_query.message.edit_text(strings.MARKET_TURNOVER_QUESTION, reply_markup=kb.TURNOVER_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.market_url)
async def handle_market_url_question_back(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(RegistrationState.market_category)
    await callback_query.message.edit_text(strings.MARKET_CATEGORY_QUESTION, reply_markup=kb.BACK_INLINE_KEYBOARD)
