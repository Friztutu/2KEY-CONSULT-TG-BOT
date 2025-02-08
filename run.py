import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.model.model import async_main
from src import router
from config import TOKEN
from src.model import requests

bot = Bot(TOKEN)

dp = Dispatcher(bot=bot)

from aiogram.types import BotCommand


def setup_scheduler():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    scheduler.add_job(
        requests.delete_old_records(),
        trigger='cron',
        hour=3,
        minute=0
    )
    return scheduler


async def on_startup():
    await asyncio.create_task(setup_scheduler())


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
    await setup_bot_commands()
    await dp.start_polling(bot)
    await on_startup()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')