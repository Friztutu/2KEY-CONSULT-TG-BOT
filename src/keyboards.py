from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔥 О нас на Wildberries", callback_data="About Wb")],
    [InlineKeyboardButton(text="🔥 О нас на Ozon", callback_data="About Ozon")],
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
    [InlineKeyboardButton(text="Ozon", callback_data="Ozon")],
    [InlineKeyboardButton(text="Wildberries", callback_data="Wb")],
    [InlineKeyboardButton(text="Ozon и Wildberries", callback_data="Ozon and Wb")],
    [InlineKeyboardButton(text="🏠 В главное меню", callback_data="start")]
])