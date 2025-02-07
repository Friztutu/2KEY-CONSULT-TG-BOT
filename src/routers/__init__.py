__all__ = ("router", )

from .commands import router as commands_router
from .registration import router as registration_router
from .info import router as info_router
from aiogram import Router

router = Router()

router.include_routers(commands_router, registration_router, info_router)
