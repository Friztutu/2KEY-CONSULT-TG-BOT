import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from src.handlers import router

load_dotenv()
bot = Bot(os.getenv('Token'))
dp = Dispatcher(bot=bot)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')