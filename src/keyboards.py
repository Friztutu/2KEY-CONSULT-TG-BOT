from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🟣 О нас на Wildberries", callback_data="About Wb")],
    [InlineKeyboardButton(text="🔵 О нас на Ozon", callback_data="About Ozon")],
    [InlineKeyboardButton(text="✏️ Оставить заявку", callback_data="register")]
])

about_ozon_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔥 Наши достижения", callback_data="Achivements Ozon")],
    [InlineKeyboardButton(text="🔥 Наши компетенции", callback_data="Competencies Ozon")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="start")]
])

about_wb_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔥 Наши достижения", callback_data="Achivements Wb")],
    [InlineKeyboardButton(text="🔥 Наши компетенции", callback_data="Competencies Wb")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="start")]
])

ozon_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✏️ Оставить заявку", callback_data="register")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="About Ozon")]
])

wb_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✏️ Оставить заявку", callback_data="register")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="About Wb")]
])

choice_market_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔵 Ozon", callback_data="Ozon")],
    [InlineKeyboardButton(text="🟣 Wildberries", callback_data="Wb")],
    [InlineKeyboardButton(text="🔵🟣 Ozon и Wildberries", callback_data="Ozon и Wildberries")],
    #[InlineKeyboardButton(text="🏠 В главное меню", callback_data="start")]
])

choice_ozon_service_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📒 Разовая консультация", callback_data="Разовая консультация")],
    [InlineKeyboardButton(text="📔 Работа с продвижением", callback_data="Работа с продвижением")],
    [InlineKeyboardButton(text="📓 Полное ведение", callback_data="Полное ведение")],
    [InlineKeyboardButton(text="📗 Полное ведение с подбором товаров", callback_data="Полное ведение с подбором товаров")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

choice_service_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📔 Работа с продвижением", callback_data="Работа с продвижением")],
    [InlineKeyboardButton(text="📓 Полное ведение", callback_data="Полное ведение")],
    [InlineKeyboardButton(text="📗 Полное ведение с подбором товаров", callback_data="Полное ведение с подбором товаров")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

choice_duration_market = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🕐 Меньше 6 месяцев", callback_data="Меньше 6 месяцев")],
    [InlineKeyboardButton(text="🕒 От 6 месяцев до года", callback_data="От 6 месяцев до года")],
    [InlineKeyboardButton(text="🕓 От года до трех лет", callback_data="От года до трех лет")],
    [InlineKeyboardButton(text="🕕 Более трех лет", callback_data="Более трех лет")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

choice_turnover_market = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💵 От 0 до 200 тыс. руб.", callback_data="От 0 до 200 тыс. руб.")],
    [InlineKeyboardButton(text="💵💵 От 200 до 500 тыс. руб", callback_data="От 200 до 500 тыс. руб")],
    [InlineKeyboardButton(text="💵💵💵 от 500 тыс. до 1 млн. руб", callback_data="от 500 тыс. до 1 млн. руб")],
    [InlineKeyboardButton(text="💵💵💵💵 от 500 тыс. до 1 млн. руб", callback_data="от 500 тыс. до 1 млн. руб")],
    [InlineKeyboardButton(text="💵💵💵💵💵 более 5 млн. руб", callback_data="более 5 млн. руб")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

choice_payment_method = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Только фиксированная оплата", callback_data="Только фиксированная оплата")],
    [InlineKeyboardButton(text="📝 Фиксированная оплата + % от прибыли", callback_data="Фиксированная оплата от прибыли")],
    [InlineKeyboardButton(text="📝 Фиксированная оплата + % от выручки", callback_data="Фиксированная оплата от выручки")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

choice_problem = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📊 Проблемы с ДРР", callback_data="Проблемы с ДРР")],
    [InlineKeyboardButton(text="📈 Хочу увеличить выручку", callback_data="Хочу увеличить выручку")],
    [InlineKeyboardButton(text="📉 Низкая рентабельность", callback_data="Низкая рентабельность")],
    [InlineKeyboardButton(text="👨‍🎓 Хочу делегировать свои задачи профессионалам", callback_data="Хочу делегировать профессионалам")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

choice_is_have_market = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Да", callback_data="Да")],
    [InlineKeyboardButton(text="❌ Нет", callback_data="Нет")],
    # [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
])

url_market_denied = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Нет магазина")]
], resize_keyboard=True, one_time_keyboard=True)

categories_denied = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пока не работаю")]
], resize_keyboard=True, one_time_keyboard=True)