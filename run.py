import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from src.model.model import async_main
from src import router
from config import TOKEN, ADMIN_USER_ID

bot = Bot(TOKEN)

dp = Dispatcher(bot=bot)

from aiogram.types import BotCommand


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/start", description="🏠 Главная страница"),
        BotCommand(command="/reg", description="✏️ Оставить заявку"),
        BotCommand(command="/about_wb", description="🟣 О нас на WildBerries"),
        BotCommand(command="/about_ozon", description="🔵 О нас на Ozon"),
        BotCommand(command="/your_request", description="📄 Посмотреть свою заявку")
    ]

    await bot.set_my_commands(bot_commands)

async def main():
    await async_main()
    dp.include_router(router)
    await setup_bot_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')