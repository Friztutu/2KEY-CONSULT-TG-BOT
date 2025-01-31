__all__ = ("router", )

from .routers import router as main_router
from aiogram import Router

router = Router(name=__name__)
router.include_routers(main_router)