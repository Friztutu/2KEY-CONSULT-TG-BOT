from aiogram import F, types
from aiogram.fsm.context import FSMContext

from src import keyboards as kb
from src.basic_funcs.validation import is_back
from src.routers.registration.base_question import router
from src.states import RegistrationState


@router.callback_query(RegistrationState.service, F.data == "Back")
async def handle_service_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.set_state(RegistrationState.marketplace)
    await callback_query.message.edit_text("Какой маркетплей вас интересует?",
                                           reply_markup=kb.MARKETPLACE_QUESTION_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.is_have_market, F.data == "Back")
async def handle_presence_market_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    await state.set_state(RegistrationState.service)
    await callback_query.message.edit_text("Выберите необходимую услугу:",
                                           reply_markup=kb.SERVICE_QUESTION_INLINE_KEYBOARD_OZON)


@router.callback_query(RegistrationState.payment_method, F.data == "Back")
async def handle_payment_method_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    types.ReplyKeyboardRemove()

    data = await state.get_data()

    if "is_have_market" in data.keys():
        await state.set_state(RegistrationState.market_url)
        await callback_query.message.delete()
        await callback_query.message.answer("Ссылка на ваш магазин?",
                             reply_markup=kb.BACK_INLINE_KEYBOARD)
    else:
        await state.set_state(RegistrationState.is_have_market)
        await callback_query.message.edit_text("У вас есть магазин?",
                                               reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)


@router.callback_query(RegistrationState.problem_type, F.data == "Back")
async def handle_problem_type_question_back(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    if data["service"] == "Разовая консультация" and data["is_have_market"] == "Нет":
        await state.set_state(RegistrationState.is_have_market)
        await callback_query.message.edit_text("У вас есть магазин?",reply_markup=kb.PRESENCE_MARKET_INLINE_KEYBOARD)
    elif data["service"] == "Разовая консультация" and data["is_have_market"] == "Да":
        await state.set_state(RegistrationState.market_url)
        await callback_query.message.edit_text("Ссылка на ваш магазин?", reply_markup=kb.BACK_INLINE_KEYBOARD)
    else:
        await state.set_state(RegistrationState.payment_method)
        await callback_query.message.edit_text("Предпочтительный режим оплаты услуг менеджера?",
                                               reply_markup=kb.PAYMENT_METHOD_INLINE_KEYBOARD)


@router.message(RegistrationState.contact, is_back)
async def handle_request_contact_back(message: types.Message, state: FSMContext) -> None:
    await state.set_state(RegistrationState.problem_type)
    await message.answer("Почему Вы решили обратиться к нам?", reply_markup=kb.CLIENT_PROBLEM_INLINE_KEYBOARDS)
