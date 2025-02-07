from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


DEFAULT_NUMBER_OF_ROWS = 1

MARKETPLACES = {"1": "Ozon", "2": "WildBerries", "3": "Ozon и WildBerries"}
SERVICES = {
    "1": "Разовая консультация",
    "2": "Работа с продвижением",
    "3": "Полное ведение",
    "4": "Полное ведение с подбором товаров"
}
IS_HAVE_MARKET = {"1": True, "2": False}
MARKET_DURATIONS = {
    None: "-", "1": "Меньше 6 месяцев", "2": "От 6 месяцев до года",
    "3": "От года до трех лет", "4": "Более трех лет"}
MARKET_TURNOVERS = {
     None: "-", "1": "От 0 до 200,000₽", "2": "От 200,000 до 500,000₽", "3": "От 500,000 до 1,000,000₽",
    "4": "От 1,000,000 до 5,000,000₽", "5": "Более 5,000,000₽"
}
PAYMENT_METHODS = {
     None: "-", "1": "Только фиксированная оплата", "2": "Фиксированная оплата + % от прибыли",
    "3": "Фиксированная оплата + % от выручки"
}
CLIENT_PROBLEMS = {
     None: "-", "1": "Проблемы с ДРР", "2": "Хочу увеличить выручку", "3": "Низкая рентабельность",
    "4": "Хочу делегировать свои задачи профессионалам"
}


# MENU & INFO INLINE KEYBOARDS
MAIN_MENU_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔵 О нас на Ozon", callback_data="About Ozon")],
    [InlineKeyboardButton(text="🟣 О нас на WildBerries", callback_data="About WB")],
    [InlineKeyboardButton(text="✏️ Оставить заявку", callback_data="Registration")]
])
ABOUT_US_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✏️ Оставить заявку", callback_data="Registration")],
    [InlineKeyboardButton(text="🏠 В главное меню", callback_data="Main Menu")]
])

# REGISTRATION INLINE KEYBOARDS
MARKETPLACE_QUESTION_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔵 Ozon", callback_data="1")],
    [InlineKeyboardButton(text="🟣 WildBerries", callback_data="2")],
    [InlineKeyboardButton(text="🔵🟣 Ozon и WildBerries", callback_data="3")],
    [InlineKeyboardButton(text="🏠 В главное меню", callback_data="Main Menu")],
])

SERVICE_QUESTION_INLINE_KEYBOARD_OZON = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📒 Разовая консультация", callback_data="1")],
    [InlineKeyboardButton(text="📔 Работа с продвижением", callback_data="2")],
    [InlineKeyboardButton(text="📓 Полное ведение", callback_data="3")],
    [InlineKeyboardButton(text="📗 Полное ведение с подбором товаров", callback_data="4")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")],
])

SERVICE_QUESTION_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📔 Работа с продвижением", callback_data="2")],
    [InlineKeyboardButton(text="📓 Полное ведение", callback_data="3")],
    [InlineKeyboardButton(text="📗 Полное ведение с подбором товаров", callback_data="4")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")],
])

PRESENCE_MARKET_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Да", callback_data="1")],
    [InlineKeyboardButton(text="❌ Нет", callback_data="2")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

MARKET_DURATION_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🕐 Меньше 6 месяцев", callback_data="1")],
    [InlineKeyboardButton(text="🕒 От 6 месяцев до года", callback_data="2")],
    [InlineKeyboardButton(text="🕓 От года до трех лет", callback_data="3")],
    [InlineKeyboardButton(text="🕕 Более трех лет", callback_data="4")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

TURNOVER_MARKET_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💵 От 0 до 200,000₽", callback_data="1")],
    [InlineKeyboardButton(text="💵💵 От 200,000 до 500,000₽", callback_data="2")],
    [InlineKeyboardButton(text="💵💵💵 От 500,000 до 1,000,000₽", callback_data="3")],
    [InlineKeyboardButton(text="💵💵💵💵 От 1,000,000 до 5,000,000₽", callback_data="4")],
    [InlineKeyboardButton(text="💵💵💵💵💵 Более 5,000,000₽", callback_data="5")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

PAYMENT_METHOD_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Только фиксированная оплата", callback_data="1")],
    [InlineKeyboardButton(text="📝 Фиксированная оплата + % от прибыли", callback_data="2")],
    [InlineKeyboardButton(text="📝 Фиксированная оплата + % от выручки", callback_data="3")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

BACK_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

CLIENT_PROBLEM_INLINE_KEYBOARDS = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Проблемы с ДРР", callback_data="1")],
    [InlineKeyboardButton(text="Хочу увеличить выручку", callback_data="2")],
    [InlineKeyboardButton(text="Низкая рентабельность", callback_data="3")],
    [InlineKeyboardButton(text="Хочу делегировать свои задачи профессионалам", callback_data="4")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])
