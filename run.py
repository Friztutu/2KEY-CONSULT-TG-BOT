import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.model.model import async_main
from src import router
from config import TOKEN, ADMIN_USER_ID
from src.model import requests as rq

bot = Bot(TOKEN)

dp = Dispatcher(bot=bot)

from aiogram.types import BotCommand


def setup_scheduler(current_bot: Bot):
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    scheduler.add_job(
        rq.delete_old_records,
        trigger='cron',
        hour=7,
        minute=10,
    )
    return scheduler

async def on_startup(current_bot: Bot):
    scheduler = setup_scheduler(current_bot)
    scheduler.start()

async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/start", description="🏠 Главная страница"),
        BotCommand(command="/reg", description="✏️ Оставить заявку"),
        BotCommand(command="/about_wb", description="🟣 О нас на WildBerries"),
        BotCommand(command="/about_ozon", description="🔵 О нас на Ozon"),
        BotCommand(command="/my_request", description="📄 Посмотреть свою заявку")
    ]

    await bot.set_my_commands(bot_commands)

async def main():
    await async_main()
    dp.include_router(router)
    await on_startup(bot)
    await setup_bot_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')