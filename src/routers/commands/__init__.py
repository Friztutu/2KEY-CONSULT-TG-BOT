__all__ = ("router", )

from aiogram import Router

from .base_commands import router as base_commands_router
from .admin_commands import router as admin_commands_router
from .manager_commands import router as manager_commands_router

router = Router()

router.include_routers(base_commands_router, admin_commands_router, manager_commands_router)