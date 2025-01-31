__all__ = ("router", )

from aiogram import Router
from .base_question import router as base_router
from .market_question import router as market_router
from .solo_consult_question import router as solo_consult_router

router = Router()

router.include_routers(base_router, market_router, solo_consult_router)