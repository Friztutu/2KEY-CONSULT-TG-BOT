__all__ = ("router", )

from aiogram import Router
from .base_question import router as base_router
from .market_question import router as market_router
from .back_handlers import router as back_router

router = Router()

router.include_routers(base_router, market_router, back_router)