__all__ = ("router", )

from .about_us import router as about_us_router
from aiogram import Router

router = Router()

router.include_routers(about_us_router, )