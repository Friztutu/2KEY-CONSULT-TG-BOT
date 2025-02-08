from aiogram.fsm.state import StatesGroup, State

class RegistrationState(StatesGroup):
    marketplace: str = State()
    service: str = State()
    payment_method: str = State()
    problem_type: str = State()
    is_have_market: str = State()
    market_duration: str = State()
    market_turnover: str = State()
    market_category: str = State()
    market_url: str = State()
    contact_method: str = State()
    contact: str = State()


class NewManagerState(StatesGroup):
    tg_id: str = State()
    first_name: str = State()


class SendAllUserState(StatesGroup):
    message: str = State()


class SendOneUserState(StatesGroup):
    tg_id: str = State()
    message: str = State()


class DeleteManagerState(StatesGroup):
    tg_id: str = State()


class TableOneDayState(StatesGroup):
    date: str = State()

