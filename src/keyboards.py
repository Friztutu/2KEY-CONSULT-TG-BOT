from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


DEFAULT_NUMBER_OF_ROWS = 1

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
    [InlineKeyboardButton(text="🔵 Ozon", callback_data="Ozon")],
    [InlineKeyboardButton(text="🟣 WildBerries", callback_data="WB")],
    [InlineKeyboardButton(text="🔵🟣 Ozon и WildBerries", callback_data="Ozon and WB")],
    [InlineKeyboardButton(text="🏠 В главное меню", callback_data="Main Menu")],
])

SERVICE_QUESTION_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📒 Разовая консультация", callback_data="Разовая консультация")],
    [InlineKeyboardButton(text="📔 Работа с продвижением", callback_data="Работа с продвижением")],
    [InlineKeyboardButton(text="📓 Полное ведение", callback_data="Полное ведение")],
    [InlineKeyboardButton(text="📗 Полное ведение с подбором товаров", callback_data="Полное ведение с подбором товаров")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")],
])

PRESENCE_MARKET_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Да", callback_data="Да")],
    [InlineKeyboardButton(text="❌ Нет", callback_data="Нет")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

MARKET_DURATION_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🕐 Меньше 6 месяцев", callback_data="Меньше 6 месяцев")],
    [InlineKeyboardButton(text="🕒 От 6 месяцев до года", callback_data="От 6 месяцев до года")],
    [InlineKeyboardButton(text="🕓 От года до трех лет", callback_data="От года до трех лет")],
    [InlineKeyboardButton(text="🕕 Более трех лет", callback_data="Более трех лет")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

TURNOVER_MARKET_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💵 От 0 до 200,000₽", callback_data="0-200000")],
    [InlineKeyboardButton(text="💵💵 От 200,000 до 500,000₽", callback_data="200000-500000")],
    [InlineKeyboardButton(text="💵💵💵 От 500,000 до 1,000,000₽", callback_data="500000-1000000")],
    [InlineKeyboardButton(text="💵💵💵💵 От 1,000,000 до 5,000,000₽", callback_data="1000000-5000000")],
    [InlineKeyboardButton(text="💵💵💵💵💵 Более 5,000,000₽", callback_data="5000000+")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

PAYMENT_METHOD_INLINE_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Только фиксированная оплата", callback_data="Фикс оплата")],
    [InlineKeyboardButton(text="📝 Фиксированная оплата + % от прибыли", callback_data="Фикс оплата + процент прибыли")],
    [InlineKeyboardButton(text="📝 Фиксированная оплата + % от выручки", callback_data="Фикс оплата + процент выручки")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="Back")]
])

# REGISTRATION REPLAY KEYBOARDS
URL_MARKET_REPLAY_KEYBOARDS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Нет магазина")],
    [KeyboardButton(text="Назад")]
], resize_keyboard=True, one_time_keyboard=True)

CATEGORIES_MARKET_REPLAY_KEYBOARDS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пока не работаю")],
    [KeyboardButton(text="Назад")]
], resize_keyboard=True, one_time_keyboard=True)

CLIENT_PROBLEM_REPLAY_KEYBOARDS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Проблемы с ДРР")],
    [KeyboardButton(text="Хочу увеличить выручку")],
    [KeyboardButton(text="Низкая рентабельность")],
    [KeyboardButton(text="Хочу делегировать свои задачи профессионалам")],
    [KeyboardButton(text="Назад")]
], resize_keyboard=True, one_time_keyboard=True)
